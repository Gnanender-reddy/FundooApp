import cgi

import jwt

from services.notes import Note

class NoteDetails:

    def create_data(self):
        print(self.headers['token'], '---->token')
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        print(payload)
        id = str(payload['id'])
        print(id, '------>id')
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
        n=Note()
        response=n.createnote(data, form_keys)
        return response

    def update_data(self):
        print(self.headers['token'], '---->token')
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        print(payload)
        id = str(payload['id'])
        print(id, '------>id')
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        form_keys = list(form.keys())
        data = {'user_id': id, 'title': form['title'].value, 'description': form['description'].value,
                'color': form['color'].value, 'ispinned': form['ispinned'].value,
                'isarchived': form['isarchived'].value, 'istrashed': form['istrashed'].value}
        n = Note()
        response=n.update(data,form_keys)
        return response

    def delete_data(self):
        print(self.headers['token'], '---->token')
        token = self.headers['token']
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        print(payload)
        id = str(payload['id'])
        print(id, '------>gnani')
        data = {'user_id': id}
        n = Note()
        response=n.delete(data)
        return response





