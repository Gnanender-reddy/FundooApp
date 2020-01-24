"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@:keyword:smtp,cgi(common graphical interface).
@Description: This code consists of api's which is used for communication between client and server.
"""
import cgi
from configuration.smtp import smtp
from model.query import DataBaseMangament
from view.response import Response
import cgitb; cgitb.enable()



class UserDetails:
    """
    This class contains api's like register, forget, setpassword etc.
    """
    def for_registration(self):
        """
        This fucntion is used for registering the data in database.

        """

        form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )

        data={'email':form['email'].value,'password':form['password'].value,'confirmpassword':form['confirmpassword'].value}
        print(data)
        data_base_object=DataBaseMangament()
        responce={'success':True,'data':[],'message':""}
        if data_base_object.password_validation(data) and data_base_object.email_validation(data['email']):
            data_base_object.registration(data)
            responce.update({'success': True, 'data': [], 'message': "Successfully registered"})
            Response(self).jsonResponse(status=200, data=responce)

        else:
             responce.update({'success':False,'data':[],'message':"not registered"})
             Response(self).jsonResponse(status=404, data=responce)


    def for_login(self):
        """
        This function is used for login process.

        """
        form=cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )
        data_base_object=DataBaseMangament()
        data={'email':form['email'].value,'password':form['password'].value}
        respon={'success':None,'data':[],'message':""}
        if data_base_object.checkinguser(data['email']) and data_base_object.checkingpassword(data['password']):

            respon.update({'success':True,'data':[],'message':"login successfull"})
            Response(self).jsonResponse(status=200,data=respon)
        else:
            respon.update({'success':False,'data':[],'message':"Login unsuccessfull"})
            Response(self).jsonResponse(status=404,data=respon)


    def forgot_password(self):
        """
        This function is used for forgot password process.
        """
        form=cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )

        data_base_object=DataBaseMangament()
        data={'email':form['email'].value}
        respon={'success':None,'data':[],'message':""}
        if data_base_object.checkinguser(data['email']):
            s = smtp()
            s.start()  # start TLS for security
            s.login()  # Authentication and login
            s.send_mail(form['email'].value)  # sending the mail

            respon.update({'success': True, 'data': [], 'message': "Message sent Successfully"})
            Response(self).jsonResponse(status=200, data=respon)
        else:

            respon.update({'success': False, 'data': [], 'message': "unsuccessfull"})
            Response(self).jsonResponse(status=404, data=respon)


    def  set_password(self,email_id):

        """
        processing user input submitted in Front end(HTML)
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'password': form['password'].value,'confirmpassword':form['confirmpassword'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) < 2:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)
        else:
            data_base_object.update_password(email_id,data['password'],data['confirmpassword'])
            responce_data.update({'success': True, 'data': [], 'message': "Password Reset successfull"})

            Response(self).jsonResponse(status=200, data=responce_data)


    def create_data(self):
        """
        This function is used for creating the data and storing the data in the database.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': True, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'title': form['title'].value, 'description': form['description'].value, 'color': form['color'].value, 'ispinned': form['ispinned'].value, 'isarchive': form['isarchive'].value, 'istrash': form['istrash'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) == 6:
            data_base_object.create_entry(data)
            responce_data.update({'success': True, 'data': [], 'message': "Entry Create Successfully"})
            Response(self).jsonResponse(status=200, data=responce_data)
        else:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)


    def update_data(self):
        """
        This update function is used for updating the data in the database.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': True, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'id': form['id'].value, 'title': form['title'].value, 'description': form['description'].value,
                'color': form['color'].value, 'ispinned': form['ispinned'].value,
                'isarchive': form['isarchive'].value, 'istrash': form['istrash'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) == 7:
            data_base_object.update(data)
            responce_data.update({'success': True, 'data': [], 'message': "Data Updated Successfully"})
            Response(self).jsonResponse(status=200, data=responce_data)
        else:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)


    def delete_data(self):
        """
        This fucntion is used for deleting the data in the database.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        respon = {'success': True, 'data': [], 'message': ""}
        data = {'id': form['id'].value}
        form_keys = list(form.keys())
        data_base_object=DataBaseMangament()
        if len(form_keys) ==1:
            data_base_object.delet(data)
            respon.update({'success': True, 'data': [], 'message': "Data delete Successfully"})
            Response(self).jsonResponse(status=200, data=respon)
        else:
            respon.update({'success': True, 'data': [], 'message': " unsuccessfull"})
            Response(self).jsonResponse(status=404, data=respon)


    def read_data(self):
        """
        This function is used for reading the data from the database.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': True, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'id': form['id'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) == 1:
            data_base_object.read(data)
            responce_data.update({'success': True, 'data': [], 'message': "Data read Successfully"})
            Response(self).jsonResponse(status=200, data=responce_data)
        else:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)



    def create_picture(self):
        """
        This function is used for creating the profile picture in the database.
        """

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success':None, 'data': [], 'message': ""}
        data = {'profile': form['profile'].value}
        data_base_object=DataBaseMangament()
        result = True
        if result:
            data_base_object.create_profile(data)
            responce_data.update({'success': True, 'data': [], 'message': "Pic saved Successfully"})
            Response(self).jsonResponse(status=200, data=responce_data)
        else:
            responce_data.update({'success': False, 'data': [], 'message': "Profile already Exist"})
            Response(self).jsonResponse(status=404, data=responce_data)

    def is_trash(self):
        """
        This function is for reading data from the database according to Trash value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        data = {'istrash': form['istrash'].value}
        responce_data = {'success': None, 'data': [], 'message': ""}
        data_base_object=DataBaseMangament()
        data_base_object.read_trash(data)
        responce_data.update({'success': True, 'data': [], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)



    def is_pinned(self):
        """
        This function is for reading data from the database according to Pinned value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None, 'data': [], 'message': ""}
        data_base_object=DataBaseMangament()
        data = {'ispinned': form['ispinned'].value}

        data_base_object.read_pin(data)
        responce_data.update({'success': True, 'data': [], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)


    def is_archive(self):
        """
        This function is for reading data from the database according to Archive value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None,'data':[],'message': ""}
        data_base_object=DataBaseMangament()
        data = {'isarchive': form['isarchive'].value}

        data_base_object.read_archive(data)
        responce_data.update({'success': True,'data':[], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)








