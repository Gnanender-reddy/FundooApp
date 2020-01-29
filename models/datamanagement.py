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


    def registration(self, data):
        """
        This function is for inserting the data to database.
        """
        print(data)
        query = "INSERT INTO users(email,password) VALUES ('" + data['email'] + "','" + data['password'] + "')"
        mydbobj.execute(query)






    def email_validation(self,email):
        """
        This function is used for checking whether entered email is in correct format or not.
        """
        regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex,email):
            return True
        else:
            return False

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

    def update_password(self, email,password, confirmpassword):
        """
        This function is used to update a password in database using sql query
        """
        query = " UPDATE users SET password = '" + password + "',confirmpassword='" + confirmpassword+ "' WHERE  email = '" + email + "' "
        return mydbobj.execute(query)

    def create_entry(self, data):
        """
        This function is used for inserting data in to data base.
        """
        query = "INSERT INTO notes(title, description, color, ispinned, isarchived, istrashed,user_id) VALUES ('" + \
                data[
                    'title'] + "', '" + data['description'] + "', '" + data['color'] + "', '" + data[
                    'ispinned'] + "', '" + data[
                    'isarchived'] + "', '" + data['istrashed'] + "','" + data['user_id'] + "')"
        return mydbobj.execute(query)
        # print("Entry create Successfully")


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
        query = "SELECT * FROM notes WHERE user_id = '" + data['id'] + "'"
        data= mydbobj.run_query(query)
        # print(data)
        return data


    def read_trash(self, data):
        """
        This function is used for reading data in which isTrash data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['istrash'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
            return x



    def read_pin(self, data):
        """
        This function is used for reading data in which isPinned data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['ispinned'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
            return x



    def read_archive(self, data):
        """
         This function is used for reading data in which isArchive data is '1'.
         """
        query = "SELECT * FROM notes WHERE " + data['isarchive'] + "=1 "
        result = mydbobj.run_query(query)
        for x in result:
            print(x)
            return x
        # print("Entry read Successfully")



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



    def validate_file_extension(self, data):
        import os
        ext = os.path.splitext(data['profile_path'])[1]  # [0] returns path+filename
        valid_extensions = ['.jpg']
        if not ext.lower() in valid_extensions:
            print("Unsupported file extension.")
        else:
            return True
            # raise ValidationError(u'Unsupported file extension.')

    def validate_file_size(self, data):
        filesize = len(data['profile_path'])
        if filesize > 10485760:
            print("The maximum file size that can be uploaded is 10MB")
        else:
            return True








