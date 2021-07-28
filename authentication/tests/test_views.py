from .setup import TestSetUp
from authentication.models import User


class TestViews(TestSetUp):
    def test_user_register_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_register(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.status_code, 201)

    def test_user_login_unverified(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_verified(self):
        res_register = self.client.post(self.register_url, self.user_data, format='json')
        email = res_register.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res_login = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(res_login.status_code, 200)
