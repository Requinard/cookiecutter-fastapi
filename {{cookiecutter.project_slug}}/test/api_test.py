from unittest import TestCase

from fastapi.testclient import TestClient

from api import api

client = TestClient(api)


class ApiTest(TestCase):
    def test_redirect(self):
        response = client.get("/", allow_redirects=False)

        self.assertEqual(response.status_code, 307)
