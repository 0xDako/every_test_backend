import os
from dotenv import load_dotenv


def load_env_data():
    load_dotenv()
    data = dict()

    data['POSTGRE_DB_NAME'] = os.getenv('POSTGRE_DB_NAME')
    data['POSTGRE_USER'] = os.getenv('POSTGRE_USER')
    data['POSTGRE_PASSWORD'] = os.getenv('POSTGRE_PASSWORD')
    data['POSTGRE_HOST'] = os.getenv('POSTGRE_HOST')
    data['POSTGRE_PORT'] = os.getenv('POSTGRE_PORT')

    return data
