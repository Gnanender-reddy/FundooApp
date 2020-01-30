import cgi

import jwt

from services.notes import Note

class NoteDetails:

    def create_data(self):
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
        note = Note()
        response=note.createnote(data, form_keys)
        return response

    def update_data(self):

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
        # condition={'user_id':id}
        data = {'user_id': id, 'title': form['title'].value, 'description': form['description'].value,
                'color': form['color'].value, 'ispinned': form['ispinned'].value,
                'isarchived': form['isarchived'].value, 'istrashed': form['istrashed'].value}
        note = Note()
        response=note.update(data,form_keys)
        return response

    def delete_data(self):
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        data = {'user_id': id}
        note = Note()
        response=note.delete(data)
        return response

    def read_data(self):
        """
        This function is used for reading the data from the database.
        """
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        id = str(payload['id'])
        data = {'user_id':id }
        note = Note()
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
        note = Note()
        response = self.pin(data)
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
        note = Note()
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
        note = Note()
        response = note.trash(data)
        return response







