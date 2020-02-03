"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Mysql connector, dotenv
@Description:This class is for my sql Data Base connection.
"""
import os
from dotenv import load_dotenv
import mysql.connector
from config.singleton import singleton
load_dotenv()

@singleton
class Database:
    """
    This class is majorly used for connecting database.
    """
    def __init__(self,**kwargs):
        self.connection=self.connect(**kwargs)
        self.mycursor = self.connection.cursor()

    def connect(self,**kwargs):
        """
        Database connection is done here.
        """
        mydb = mysql.connector.connect(
                host=kwargs["host"],
                user=kwargs["user"],
                passwd=kwargs["passwd"],
                database=kwargs["database"]
        )
        return mydb
        # self.mycursor = self.mydb.cursor()

    def run_query(self, query):
        """
        This function is used for running the query and fetching data from database.
        """

        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def execute(self, query,value=None):
        """
        This function is for executing query and commiting data to database.
        """

        self.mycursor.execute(query,value)
        self.connection.commit()

database= Database(host=os.getenv("HOST"),
                    user=os.getenv("USER_DB"),
                    passwd=os.getenv("PASSWD"),
                    database=os.getenv("DATABASE"))
