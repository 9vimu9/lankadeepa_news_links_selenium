import os
import string
import mysql.connector
from mysql.connector import Error

class Connection:
    
    def __init__(self):
        self.__connection = None
        self.__cursor = None
        self.__create()
    

    def __create(self):
        try:
            connection = mysql.connector.connect(
                host = os.getenv('MY_SQL_HOST'), 
                database=os.getenv('MY_SQL_DATABASE'),
                user = os.getenv('MY_SQL_USER'), 
                password = os.getenv('MY_SQL_PASSWORD'), 
                port = os.getenv('MY_SQL_PORT')
                )
            if connection.is_connected():
                self.__connection = connection
                cursor = connection.cursor()
                self.__cursor = cursor

        except Error as e:
            print("Error while connecting to MySQL", e)
       
        
    
    def __close(self):
            
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()
    

    def execute(self,query:string):
            self.__cursor.execute(query)
            record =  self.__cursor.fetchall()
            self.__close()
            return record




    @staticmethod
    def query(query:string):
        return (Connection()).execute(query)




# The Google Python Style Guide has the following convention:
    # module_name, 
    # package_name, 
    # ClassName, 
    # method_name, 
    # ExceptionName, 
    # function_name, 
    # GLOBAL_CONSTANT_NAME, 
    # global_var_name, 
    # instance_var_name, 
    # function_parameter_name, 
    # local_var_name