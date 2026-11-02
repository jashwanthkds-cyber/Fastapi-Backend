# Fastapi-Backend

STEP-1: -Creating and Setting Up the E-Commerce Project

      create a repo github repo and clone to antgravity or vs code.
      create venv and activate it.

Then:
       Install requirement.txt and create the main.py in the app folder

       In the main.py Step-1: This lines import fastapi and create an instance of the FastAPI class.(1-16)

STEP-2: Connecting the E-Commerce Project to PostgreSQL
        
        create env file and define the database_url and more in .env file
        name:Electronic-ecommerce
        And create the db folder in app and create session.py

Then:    
        create database url and create engine in session.py Step-2 line(1-7)   

        Step-3
        create the common/dependecies.py 
        create the function get_db() line (1-8)
        create core/config.py
        and install pydantic_settings
        And line(1-10).
        In the session  import settings from config.