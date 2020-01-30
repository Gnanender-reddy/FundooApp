"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for managing database.
"""
from config.connection import database
import re
mydbobj=database


class DataBaseMangament:
    """
    This class is used to form connection with the database and perform operation update, add and check
    entry into the database
    """
    def __init__(self):
        """
        This function is used to form a connection with database
        """
        pass

    def user_insert(self, data, table_name=None):
        table_name = table_name
        column = []
        rows_values = []
        val = []
        for key, value in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(value)
        column = ', '.join(column)
        val_ = ', '.join(['%s'] * len(val))
        print(column)
        print(rows_values)
        print(val)
        query = '''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
        print(query)
        mydbobj.execute(query=query, value=val)


    def read_email(self, email=None):
        id = None
        sql = "SELECT email,id FROM users where email = '" + email + "'"
        result = mydbobj.run_query(sql)
        print(result)
        print(email, id)
        if result is not None:
            email, id = result[0]
            return id, email
        else:
            return None

    def checkinguser(self, email):
        """
        This function is used for whether provided email is in database or not.
        """
        query = "select * from users where email = '" + email + "'"
        result = mydbobj.run_query(query)
        id=result[0][0]
        if id:
            return id
        else:
            return False

    def checking_email(self,email):
        query="select * from users where email='"+email+"'"
        result=mydbobj.run_query(query)
        if result:
            return True
        else:
            return False


    def checkingpassword(self,password):
        """
        This is  used for whether password is present or not.
        """
        query="select password from users where password='" + password+ "'"
        result=mydbobj.run_query(query)
        if result:

            return True
        else:
            return False

    def update_password(self, email_id,password):
        """
        This function is used to update a password in database using sql query
        """
        query = " UPDATE users SET password = '" + password + "' WHERE  email = '" + email_id + "' "
        return mydbobj.execute(query)



    def update(self, data):
        """
        This function is used for updating the data in the database.
        """
        query = "UPDATE notes SET title = '" + data['title'] + "',description = '" + data[
            'description'] + "',color = '" + data['color'] + "',ispinned = '" + data[
                    'ispinned'] + "', isarchived = '" + data['isarchived'] + "', istrashed = '" + data[
                    'istrashed'] + "' WHERE  user_id = " + data['user_id'] + ""
        mydbobj.execute(query)
        print("Data update Successfully")


    def delete(self,data):
        """
        This function is used for deleting the data in the database based on id.
        """
        query="delete from notes WHERE  user_id = " + data['user_id'] + ""
        mydbobj.execute(query)


    def read(self, data):
        """
        This function is used for reading the data from database
        """
        query = "SELECT * FROM notes WHERE user_id = '" + data['user_id'] + "'"
        data= mydbobj.run_query(query)
        return data


    def read_trash(self, data):
        """
        This function is used for reading data in which isTrash data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['istrash'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
        return len(result)



    def read_pin(self, data):
        """
        This function is used for reading data in which isPinned data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['ispinned'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
        return len(result)



    def read_archive(self, data):
        """
         This function is used for reading data in which isArchive data is '1'.
         """
        query = "SELECT * FROM notes WHERE " + data['isarchive'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
        return len(result)




    def profile_exist(self, data):
        """
        This function is used for checking profile if it is exist or not.

        """

        query = "SELECT * from profile where user_id = '" + data['user_id'] + "'"
        result = mydbobj.run_query(query)
        print(result)
        if len(result):
                return False
        else:
                return True



    def create_pic(self, data):
            query = "INSERT INTO profile(profile_path, user_id)VALUES('" + data['profile_path'] + "','" + data[
            'user_id'] + "')"
            mydbobj.execute(query)
            return {'success': True, 'data': [], 'message': "Pic saved Successfully"}



    def user_insert(self, data, table_name=None):
        table_name = table_name
        column = []
        rows_values = []
        val = []
        for key, value in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(value)
        column = ', '.join(column)
        val_ = ', '.join(['%s'] * len(val))
        print(column)
        print(rows_values)
        print(val)
        query = '''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
        print(query)
        mydbobj.execute(query=query, value=val)

    def updatee(self, data, table_name=None, condition=None):
        column = []
        rows_values = []
        val = []
        for key, value in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(value)
        column1 = []
        rows_values1 = []
        val1 = []
        for key1, value1 in condition.items():
            column1.append(key1)
            rows_values1.append("%s")
            val1.append(value1)
        terms = ' , '.join(f'{key} = %s' for key in data)
        query = 'UPDATE %s SET ' % table_name + terms + ' WHERE %s = %s' % (column1[0], val1[0])
        mydbobj.execute(query=query, value=val)













