# CRUD-FastApi
Implemented CRUD operations using FastApi and Postgres

Steps to SetUp and Run the App:-

Step1:-  Install PostgresQL and PGAdmin as Gui for PostgresQL for database usuage.
Step2:-  Create a School database containing table studens which has field as given below
        CREATE TABLE students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            grade VARCHAR(10) NOT NULL
        );

Step3:- Insert some data to check whether we are able to fetch it using query.
Step4:- We will need a connector for postgres and we have used "psycopg2" as a python connector.
Step5:- Implement utility function for connecting to a database and executing the query.
Step6:- Implement CRUD function to create update read and delete student.
Step7:- Implement Endpoint for each operations having different usuage.
Step8:- To run the application in IDE go to the terminal containing the file and apply below command to the
        app will run as a localhost connected to DB.
        Command:- uvicorn main:app --reload
Step9:- Install Postman as a tool to run the endpoints and check whether we are able to implement CRUD operations and url and body
        for the request are as follows:-
        GET ALL API:- 
            URL:- http://localhost:8000/students/
        GET BY ID API:- 
            URL:- http://localhost:8000/students/2
        POST API:- 
            URL:- http://localhost:8000/students/
            BODY:- {
                        "name": "Dikshant",
                        "age": 24,
                        "grade": "A"
                    }
        PUT API:-
            URL:- http://localhost:8000/students/6
            BODY:- {
                        "name": "Dikshant P",
                        "age": 23,
                        "grade": "A+"
                    }
        DELETE API:-
            URL:- http://localhost:8000/students/6
