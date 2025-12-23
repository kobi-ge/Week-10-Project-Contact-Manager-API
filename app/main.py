from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import mysql.connector

import data_interactor as di
from contact import Contact


class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

app = FastAPI()

db = di.SqlManager()

@app.get("/contacts")
def get_contacts():
    query = "SELECT * FROM contacts"
    return db.select(query)

@app.post("/contacts")
def add_contact(schema: ContactSchema):
    new_contact_obj = Contact(
        first_name=schema.first_name,
        last_name=schema.last_name,
        phone_number=schema.phone_number
    )
    contact_dict = new_contact_obj.to_dict()
    query = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
    params = (contact_dict['first_name'], contact_dict['last_name'], contact_dict['phone_number'])
    new_id = db.insert(query, params)
    return {"id": new_id, "message": "Created successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


