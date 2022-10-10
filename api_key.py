import dotenv
import os


def get_key():
    dotenv.load_dotenv('./config.env')
    return str(os.getenv('NASA_API_KEY'))

