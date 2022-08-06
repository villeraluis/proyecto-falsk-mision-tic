from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_CONNECTION_URI = 'sqlite:///database/hotel.db'

print(DATABASE_CONNECTION_URI)
