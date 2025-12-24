import mysql.connector
import os
from dotenv import load_dotenv
import time

load_dotenv()

class SqlManager:
    def __init__(self):
        self.db = None
        self.cursor = None
        retries = 10
        delay = 3

        while retries > 0:
            try:
                self.db = mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    port=os.getenv('DB_PORT'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),
                    database=os.getenv('DB_NAME')
                )
                self.cursor = self.db.cursor(dictionary=True)
                print("Connected to database successfully")
                return  
            
            except mysql.connector.Error as err:
                print(f"Connection failed ({retries} retries left): {err}")
                retries -= 1
                time.sleep(delay)

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
