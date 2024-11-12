Aarti's Django Project for CRUD Operations
This project is a simple CRUD application built with Django, featuring a PostgreSQL backend. 
It includes separate frontend and backend directories and provides all essential registration information.

<----------------Project Setup--------------------->

1. Clone the Repository
To begin, clone the repository to your local machine:
    git clone https://github.com/Aarti-Sharma05/Aarti_assessment.git
    cd Aarti_assessment
   
2. Install dependencies
   Required Software :
   i. Python - download python
   ii. Django- pip install django
   iii. psycopg2- pip install psycopg2 (allows django project to interact with postgresql database)
   iv. PostgreSql- download PostgreSql
   
3.Database Setup
   This project uses PostgreSQL database and it is already configured in Django project.
   Open the postgresql shell:
      Login as postgres
      Create the database using following command: 
         CREATE DATABASE mydatabase;
         CREATE USER myuser WITH PASSWORD 'mypassword';
         GRANT ALL PRIVILEGES ON DATABASE TO mydatabase TO myuser;

4. Running the project
    i. Apply migrations- Run migrations to set up the database table by following command: 
             python manage.py migrate
    ii. Create superuser- Access the admin panel of django by following command :
             python manage.py createsuperuser
        Enter username,email and password
    iii. Start the server by following command: 
             python manage.py runserver
             Visit http://127.0.0.1:8000/ in your browser to access the project.

<------------Functionality Working------->
(On home page list of Registered user will be shown in a table.)

1. To perform Create operations in navbar click on Register User.
2. To perform Read operation click on Name of the user.
3. To perform Update operation click on Name of the registered user ( update is mentioned).
4. To perform Delete operation click on Name of the registered user (delete option is mentioned).

---------Features-------
Create, Read, Update, Delete (CRUD) operations on registration data.
PostgreSQL database integration for reliable data storage.
User-friendly frontend to interact.

<-------------FEEL FREE TO REACH OUT---------------------->


   
   

