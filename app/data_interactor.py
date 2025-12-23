import mysql.connector

class SqlManager:
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123"
        )

    def select(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        return response
    
    def CUD_operations(self, sql):
        mycursor = self.db.cursor()
        mycursor.execute(sql)
        self.db.commit()


    # def update(self, sql):
    #     mycursor = self.db.cursor()
    #     mycursor.execute(sql)
    #     self.db.commit()

    # def insert(self, sql):
    #     mycursor = self.db.cursor()
    #     mycursor.execute(sql)
    #     self.db.commit()

    # def delete(self, sql):
    #     mycursor = self.db.cursor()
    #     mycursor.execute(sql)
    #     self.db.commit()