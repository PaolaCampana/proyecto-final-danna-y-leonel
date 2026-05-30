import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

def get_connection():

    return mysql.connector.connect(

      os.getenv("DB_HOST")
      os.getenv("DB_PORT")
      os.getenv("DB_USER")
      os.getenv("DB_PASSWORD")
      os.getenv("DB_NAME")


    )
