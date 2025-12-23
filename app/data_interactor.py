import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class SqlManager:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host = os.getenv('DB_HOST'),
                user = os.getenv('DB_USER'),
                password = os.getenv('DB_PASSWORD'),
                database = os.getenv("DB_NAME")
            )
            print("connected to MySql database successfully")
        except mysql.connector.error as err:
            print(f"Error connecting to database: {err}")

    def select(self, query, params=()):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, params)
        response = cursor.fetchall()
        cursor.close()
        return response

    def update(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()
        cursor.close()

    def insert(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id

    def delete(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()
        cursor.close()
