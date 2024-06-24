import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def initialize_database():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    is_admin BOOLEAN NOT NULL
                );
                CREATE TABLE IF NOT EXISTS check_ins (
                    id SERIAL PRIMARY KEY,
                    username TEXT NOT NULL,
                    check_in_time TIMESTAMP NOT NULL,
                    check_out_time TIMESTAMP
                );
            ''')
            conn.commit()

def add_user_to_db(username, password_hash, is_admin):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO users (username, password_hash, is_admin) VALUES (%s, %s, %s)', (username, password_hash, is_admin))
            conn.commit()

def authenticate_user(username, password_hash):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE username=%s AND password_hash=%s', (username, password_hash))
            user = cursor.fetchone()
            return user is not None

def is_admin_user(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT is_admin FROM users WHERE username=%s', (username,))
            user = cursor.fetchone()
            return user and user[0]

def get_user(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
            user = cursor.fetchone()
            if user:
                return {'id': user[0], 'username': user[1], 'password_hash': user[2], 'is_admin': user[3]}
            return None

def get_all_users():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            return [{'id': user[0], 'username': user[1], 'password_hash': user[2], 'is_admin': user[3]} for user in users]

def get_user_check_ins(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM check_ins WHERE username=%s ORDER BY check_in_time DESC', (username,))
            check_ins = cursor.fetchall()
            return [
                {
                    'id': check_in[0],
                    'username': check_in[1],
                    'check_in_time': check_in[2].strftime('%H:%M - %d/%m/%Y'),
                    'check_out_time': check_in[3].strftime('%H:%M - %d/%m/%Y') if check_in[3] else 'N/A'
                }
                for check_in in check_ins
            ]

def get_open_check_in(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM check_ins WHERE username=%s AND check_out_time IS NULL ORDER BY check_in_time DESC LIMIT 1', (username,))
            check_in = cursor.fetchone()
            if check_in:
                return {'id': check_in[0], 'username': check_in[1], 'check_in_time': check_in[2], 'check_out_time': check_in[3]}
            return None

def insert_check_in(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO check_ins (username, check_in_time) VALUES (%s, %s)', (username, datetime.now()))
            conn.commit()

def update_check_out(check_in_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('UPDATE check_ins SET check_out_time=%s WHERE id=%s', (datetime.now(), check_in_id))
            conn.commit()

def close_connection():
    with get_connection() as conn:
        conn.close()

# Initialize the database tables if they don't exist
initialize_database()
