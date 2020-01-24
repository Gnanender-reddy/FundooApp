"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Mysql connector, dotenv
@Description:This class is for my sql Data Base connection.
"""
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
class Database:
    """
    This class is majorly used for connecting database.
    """
    def connection(self):
        """
        Initializing database with user's credentials and these credentials are not seen because they are stored in dote
        -nv file, this dotenv file is for security purpose.
        """

        mydb = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            passwd=os.getenv("passwd"),
            database=os.getenv("database")
        )
        return mydb
        # self.mycursor = self.mydb.cursor()

    def run_query(self, query):
        """
        This function is used for running the query and fetching data from database.
        """
        database=Database
        mydb=database.connection(self)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        return mycursor.fetchall()

    def execute(self, query):
        """
        This function is for executing query and commiting data to database.
        """
        database = Database
        mydb = database.connection(self)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
