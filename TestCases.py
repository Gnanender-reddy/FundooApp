import json
import unittest
from audioop import reverse
import requests
import jsonpath
import socket


from nltk import app, sys

from view.credentials import details
sys.path.append("../..")


class MyTestCase(unittest.TestCase):



    # def test_register(self):
    #     data = {'email': 'gnanend@gmail.com', 'password': "122", 'confirmpassword': "122"}
    #     d1 = details()
    #     d1.register(data)
    #     self.assertEqual("success")
    # def setup(self):
    #     app.app.config['TESTING'] = True
    #     self.app = app.app.test_client()

    # def test_output(self):
    #     d1 = details()
    #     with app.test_request_context():
    #         # moc
    #         out = d1.register('error', 'Test Error', 'local_host')
    #
    #         response = [
    #             {
    #                 'type': 'error',
    #                 'message': 'Test Error',
    #                 'download_link': 'local_host'
    #             }
    #         ]
    #         data = json.loads(out.get_data(as_text=True))
    #         # Assert response
    #         self.assertEqual(data['response'], response)
    def setUp(self):

        details.objects.create( email='asd123@gmail.com', password='As123456',confirmpassword='As123456')
        # details.objects.create(username='rameshboini', email='asdf123@gmail.com', password='As1234',)

    def test_register(self):
        email = details.objects.get(email='asdf123@gmail.com')
        password = details.objects.get(password='As123456')
        confirmpassword = details.objects.get(confirmpassword='As123456')
        self.assertEqual(email,password,confirmpassword,'registered successsfully')





if __name__ == '__main__':
    unittest.main()
