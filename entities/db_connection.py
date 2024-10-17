import pymysql
import sqlite3


class Database:
    @staticmethod
    def connect():
        # Establishes and returns a connection to the MySQL database
        return pymysql.connect(
            host='localhost',
            user='root',
            password='Lonewolf@31',
            database='weather_website'
        )

    @staticmethod
    def execute_query(query, params=()):
        """Executes a query with the given parameters."""
        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            conn.close()
            return cursor.rowcount
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    @staticmethod
    def fetch_one(query, params=()):
        """Fetches a single record from the database."""
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def fetch_all(query, params=()):
        """Fetches all records from the database."""
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
