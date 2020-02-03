"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This class is for fetching the notes data from users.
"""

import cgi
import jwt
from services.notes_services import NoteServices

class NoteDetails:
    """
    This class is for fetching the notes data from users.
    """

    def create_data(self):
        """
        This function is used for fetching notes from user.
        """
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        form_keys = list(form.keys())
        data = {'title': form['title'].value, 'description': form['description'].value, 'color': form['color'].value,
                'ispinned': form['ispinned'].value, 'isarchived': form['isarchived'].value,
                'istrashed': form['istrashed'].value, 'user_id': id}
        note = NoteServices()
        response=note.createnote(data, form_keys)
        return response

    def update_data(self):
        """
        This function is used for updating notes of particular user.
        """

        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        form_keys = list(form.keys())
        condition={'user_id': id,}
        data = { 'title': form['title'].value, 'description': form['description'].value,
                'color': form['color'].value, 'ispinned': form['ispinned'].value,
                'isarchived': form['isarchived'].value, 'istrashed': form['istrashed'].value}
        note = NoteServices()
        response=note.update(data,condition,form_keys)
        return response

    def delete_data(self):
        """
        This function is used for deleting the notes of user.
        """
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        data = {'user_id': id}
        note = NoteServices()
        response=note.delete(data)
        return response

    def read_data(self):
        """
        This function is used for reading notes of user.
        """
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        data = {'user_id':id }
        note = NoteServices()
        response = note.readd(data)
        return response



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

        data = {'ispinned': form['ispinned'].value}
        note = NoteServices()
        response = note.pin(data)
        return response


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

        data = {'isarchive': form['isarchive'].value}
        note = NoteServices()
        response = note.archive(data)
        return response



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
        note = NoteServices()
        response = note.trash(data)
        return response







