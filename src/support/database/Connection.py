import os
import string
import sys
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
                self.__cursor = connection.cursor()

        except Error as e:
            print("Error while connecting to MySQL", e)
       
        
    
    def __close(self):
            
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()
    

    def execute(self,query:string):
        self.__cursor.execute(query)
        record =  self.__cursor.fetchall()#if no record return empty list
        self.__close()
        return record

    def insert_execute(self,table:string,key_value_pair:dict):

        try:
            placeholders = ', '.join(['%s'] * len(key_value_pair))
            columns = ', '.join(['`{}`'.format(value) for value in key_value_pair.keys()])
            sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
            self.__cursor.execute(sql, list(key_value_pair.values()))
            self.__connection.commit()
            last_row_id =  self.__cursor.lastrowid
            self.__close()
            return last_row_id
            
        except Exception as e: 
            return False

    def update_by_id_execute(
        self,
        table:string,
        id:int,
        key_value_pair:dict)->bool:

        try:
            updatables = ','.join(["`%s` = '%s'" % (key, value) for (key, value) in key_value_pair.items()])
            sql = "UPDATE %s SET  %s  WHERE id = %s" % (table, updatables, id)
            self.__cursor.execute(sql)
            self.__connection.commit()
            self.__close()
            return True
            
        except Exception as e: 
            return False



    @staticmethod
    def query(query:string):
        return (Connection()).execute(query)

    @staticmethod
    def insert(table:string,key_value_pair:dict):
        return (Connection()).insert_execute(table,key_value_pair)

    @staticmethod
    def update_by_id(table:string,id:int,key_value_pair:dict)->bool:
        return (Connection()).update_by_id_execute(table,id,key_value_pair)





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