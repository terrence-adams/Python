import requests
import json


class Post:
    login_url = 'https://dev.sync1creditservices.com/api/Login'

    def __init__(self):
        with requests.Session() as self.s:
            self.l = self.s.post(self.login_url, headers={'Content-type': 'application/json-patch+json', 'accept':'text/plain'},
                                 json={'username': 'loan.officer@cua.com', 'password': 'sync1test'})
            self.resp_dict = json.loads(self.l.text)
            self.token = self.resp_dict['token']['access_token']

    def log_in(self):
        print(self.l.headers)
        print(self.l.status_code)
        print(self.l.text)
        print(self.l.url)
        print(self.l.json())
        print(self.token)

    def get_token(self):
        return self.token




if __name__ == '__main__':
    p = Post()
    p.log_in()