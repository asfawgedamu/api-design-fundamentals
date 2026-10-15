
# config.py — Configuration for the FastAPI project
# This file loads environment variables from a .env file and provides configuration settings for the application. 
# It uses the python-dotenv package to manage environment variables securely.
# To use this configuration, ensure you have a .env file in the root of your project with the following variables:
# SECRET_KEY=your_secret_key_here   
# API_KEY=your_api_key_here
# DATABASE_URL=your_database_url_here


from dotenv import load_dotenv     #Load environment variables from the .env file

import os                          # Import the os module to access environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")      # Load the SECRET_KEY from environment variables
API_KEY = os.getenv("API_KEY")            # Load the API_KEY from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")  # Load the DATABASE_URL from environment variables