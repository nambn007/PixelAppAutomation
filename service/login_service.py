import requests

PIXEL_LOGIN_API='http://127.0.0.1:8000/api/'

class LoginService:

    def __init__(self) -> None:
        self.login_api = PIXEL_LOGIN_API + "login/"
        self.isauth_api = PIXEL_LOGIN_API + "isauth/"

    def login(self, user, password):
        payload = {
            'username': user,
            'password': password
        }
        response = requests.request('POST', self.login_api, headers={}, data=payload)
        return response.text 
    
    def isauth(self, token):
        headers = {
            'Authorization': f'Token {token}'
        }
        response = requests.request('GET', url=self.isauth_api, headers=headers)
        return response.text