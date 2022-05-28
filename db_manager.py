import sqlite3
import psycopg2
from psycopg2 import Error

from scheamas import * 

class DBManager():
    
    def __init__(self, env_data) -> None:
        try:
            self.env_data = env_data
            self.connection = psycopg2.connect(dbname=env_data['POSTGRE_DB_NAME'], user=env_data['POSTGRE_USER'],
                                            password=env_data['POSTGRE_PASSWORD'], host=env_data['POSTGRE_HOST'],
                                            port=env_data['POSTGRE_PORT'])
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print("Error when working with PostgreSQL: ", error)
    
    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection with PostgreSQL is closed")

    def __handle_injection(self, sql_request, parameters):
        try:
            self.cursor.execute(sql_request, tuple(parameters))
        except (Exception, Error) as error:
            print(error)
            if type(error) == psycopg2.errors.InvalidTextRepresentation:
                print('Incorrect function parameters (SQL injection)')
            self.cursor.execute("ROLLBACK")
        finally:
            self.connection.commit()
    
    def get_test(self, invite_code : str):
        sql_request =   '''
                        SELECT * FROM tests WHERE invite_code = %s;
                        '''
        parameters = (invite_code,)
        self.__handle_injection(sql_request, parameters)
        
        if self.cursor.rowcount <= 0:
            return []
        else:
            return self.cursor.fetchall()[0]
    
    def get_questions(self, test_id : int):
        sql_request =   '''
                        SELECT * FROM questions WHERE test_id = %s ORDER BY question_id
                        '''
        parameters = (test_id,)

        self.__handle_injection(sql_request, parameters)

        if self.cursor.rowcount <= 0:
            return []
        else:
            return self.cursor.fetchall()
    
    def add_user_result(self, user_name, test_id, result):
        sql_request =   '''
                        INSERT INTO test_results (name, test_id, result) VALUES (%s, %s, %s)
                        '''
        parameters = (user_name, test_id, result)
        self.__handle_injection(sql_request, parameters)

        return {}