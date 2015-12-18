from django.test import TestCase, Client


class HelloWorldTest(TestCase):
    def test_reply_hello_world(self):
        # create client
        client = Client()

        # request '/'
        response = client.get('/')

        # test response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world!')
