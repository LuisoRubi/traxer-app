from dotenv import load_dotenv
import os

load_dotenv

MONGO_URI = osgetenv("MONGO_URI")
DB_NAME = "traxer-app"