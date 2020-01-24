"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for managing database.
"""
import base64
from configuration.connection import Database
import re


class DataBaseMangament:
    """
    This class is used to form connection with the database and perform operation update, add and check
    entry into the database
    """
    def __init__(self):
        """
        This function is used to form a connection with database
        """
        self.mydbobj = Database()


    def registration(self, data):
        """
        This function is for inserting the data to database.
        """
        print(data)
        query = "INSERT INTO users(email,password,confirmpassword) VALUES ('" + data['email'] + "','" + data['password'] + "','" + data['confirmpassword'] + "')"
        self.mydbobj.execute(query)


    def password_validation(self,data):
        """
         This function is used to checking whether password and confirm password are same.
        """
        if data['password'] == data['confirmpassword']:
            return True
        else:
            return False


    def email_validation(self,email):
        """
        This function is used for checking whether entered email is in correct format or not.
        """
        regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex,email):
            return True
        else:
            return False

    def checkinguser(self, email):
        """
        This function is used for whether provided email is in database or not.
        """
        query = "select email from users where email = '" + email + "'"
        result = self.mydbobj.run_query(query)
        if result:
            return True
        else:
            return False


    def checkingpassword(self,password):
        """
        This is  used for whether password is present or not.
        """
        query="select password from users where password='" + password+ "'"
        result=self.mydbobj.run_query(query)
        if result:

            return True
        else:
            return False

    def update_password(self, email,password, confirmpassword):
        """
        This function is used to update a password in database using sql query
        """
        query = " UPDATE users SET password = '" + password + "',confirmpassword='" + confirmpassword+ "' WHERE  email = '" + email + "' "
        return self.mydbobj.execute(query)

    def create_entry(self, data):
        """
        This function is used for inserting data in to data base.
        """
        query = "INSERT INTO notes(title, description, color, ispinned, isarchive, istrash) VALUES ('" + \
                data[
                    'title'] + "', '" + data['description'] + "', '" + data['color'] + "', '" + data[
                    'ispinned'] + "', '" + data[
                    'isarchive'] + "', '" + data['istrash'] + "')"
        return self.mydbobj.execute(query)
        # print("Entry create Successfully")


    def update(self, data):
        """
        This function is used for updating the data in the database.
        """
        query = "UPDATE notes SET title = '" + data['title'] + "',description = '" + data[
            'description'] + "',color = '" + data['color'] + "',ispinned = '" + data[
                    'ispinned'] + "', isarchive = '" + data['isarchive'] + "', istrash = '" + data[
                    'istrash'] + "' WHERE  id = " + data['id'] + ""
        self.mydbobj.execute(query)
        print("Data update Successfully")


    def delet(self,data):
        """
        This function is used for deleting the data in the database based on id.
        """
        query="delete from notes WHERE  id = " + data['id'] + ""
        self.mydbobj.execute(query)


    def read(self, data):
        """
        This function is used for reading the data from database
        """
        query = "SELECT * FROM notes WHERE id = '" + data['id'] + "'"
        data= self.mydbobj.run_query(query)
        # print(data)
        return data


    def read_trash(self, data):
        """
        This function is used for reading data in which isTrash data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['istrash'] + "=1 "
        result = self.mydbobj.run_query(query)
        for x in result:
            print(x)
            return x



    def read_pin(self, data):
        """
        This function is used for reading data in which isPinned data is '1'.
        """
        query = "SELECT * FROM notes WHERE " + data['ispinned'] + "=1 "
        result = self.mydbobj.run_query(query)
        for x in result:
            print(x)
            return x



    def read_archive(self, data):
        """
         This function is used for reading data in which isArchive data is '1'.
         """
        query = "SELECT * FROM notes WHERE " + data['isarchive'] + "=1 "
        result = self.mydbobj.run_query(query)
        for x in result:
            print(x)
            return x
        # print("Entry read Successfully")



    def profile_exist(self, data):
        """
        This function is used for checking profile if it is exist or not.

        """
        image = base64.b64encode(data['profile'])
        valid_image = image.decode("utf-8")
        query = "SELECT * from ProfilePicture where image = '" + valid_image + "'"
        result = self.mydbobj.run_query(query)
        print(result)
        if len(result):
                return False
        else:
                return True



    def create_profile(self, data):
        """
        This function is used for creating profile picture and sending in to database.
        """
        image = base64.b64encode(data['profile'])
        valid_image = image.decode("utf-8")
        query = "INSERT INTO ProfilePicture(image) VALUES('" + valid_image + "')"
        self.mydbobj.execute(query)
        print("Entry create Successfully")





