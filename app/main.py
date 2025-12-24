from fastapi import FastAPI, HTTPException
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

@app.put("/contacts/{id}")
def update_contact(id: int, schema: ContactSchema):
    try:
        check_query = "SELECT * FROM contacts WHERE id = %s"
        if not db.select(check_query, (id,)):
            raise HTTPException(status_code=404, detail="Contact not found")
        
        contact_obj = Contact(first_name=schema.first_name, last_name=schema.last_name, phone_number=schema.phone_number, contact_id=id)
        contact_dict = contact_obj.to_dict()
        query = """UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s"""
        params = (contact_dict['first_name'], contact_dict['last_name'], contact_dict['phone_number'], id)
        db.update(query, params)
        return {"message": f"Contact {id} updated successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/contacts/{id}")
def delete_contact(id: int):
    try:
        check_query = "SELECT * FROM contacts WHERE id = %s"
        if not db.select(check_query, (id,)):
            raise HTTPException(status_code=404, detail="Contact not found")
        
        delete_query = "DELETE FROM contacts WHERE id = %s"
        db.delete(delete_query, (id,))
        return {"message": f"Contact {id} deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


