Contact Management REST API!
מערכת ניהול אנשי קשר!

A REST API application built with Python and FastAPI for managing a contact list, backed by a MySQL database. The entire application is containerized using Docker and Docker Compose.

###API Endpoints
GET  '/contacts' - Retrieve all contacts.
POST '/contacts' - Create a new contact.
PUT '/contacts{id}' - Update an existing contact.
DELETE '/contacts{id}' - elete a contact.

### Setup Instructions

Docker Desktop installed and running.


### How to run
1. Open a terminal in the project directory.

2. Run the following command to build and start the containers:
   docker compose up --build -d

3. Important Note:
   When running for the first time, please wait about 30 seconds for the database to initialize and import the sample data before sending requests.

### Testing Instructions

You can verify the API is working using the following curl commands in your terminal:

1. Get all contacts:
   curl http://localhost:8000/contacts

2. Create a new contact:
   curl -X POST http://localhost:8000/contacts -H "Content-Type: application/json" -d "{\"first_name\": \"Test\", \"last_name\": \"User\", \"phone_number\": \"050-0000000\"}"

3. Update a contact (replace 1 with an actual ID):
   curl -X PUT http://localhost:8000/contacts/1 -H "Content-Type: application/json" -d "{\"first_name\": \"Updated\", \"last_name\": \"Name\", \"phone_number\": \"050-1111111\"}"

4. Delete a contact (replace 1 with an actual ID):
   curl -X DELETE http://localhost:8000/contacts/1

### Persistence Check
To verify data is saved:
1. Create a contact.
2. Run: docker compose down
3. Run: docker compose up -d
4. Check if the contact still exists using the GET command.