import mysql.connector

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "",
    "database": "building2026_pu",
    "charset": "utf8mb4",
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)