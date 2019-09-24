import requests
import json


class Post:
    login_url = 'https://dev.sync1creditservices.com/api/Login'
    preview_login_url = 'https://preview.sync1creditservices.com/api/Login'
    credit_url = 'https://dev.sync1creditservices.com/api/Credit'
    preview_credit_url = 'https://preview.sync1creditservices.com/api/Credit'
    BEARER = 'bearer '  # constant
    credit_response = None
    token = ''

    def __init__(self):
        with requests.Session() as self.s:
            self.l = self.s.post(self.preview_login_url, headers={'Content-type': 'application/json-patch+json', 'accept':'text/plain'},
                                 json={'username': 'sync1@cuanswers.com', 'password': 'Testsync1'})
            self.resp_dict = json.loads(self.l.text)
            self.token = self.resp_dict['token']['access_token']
            self.header = {}
            self.body = {}
            print(self.token)

    # used for development
    def log_in(self):
        print(self.l.headers)
        print(self.l.status_code)
        print(self.l.text)
        print(self.l.url)
        print(self.l.json())
        print(self.token)

    #supporter method
    def get_token(self):
        return self.token

    # supporter method
    def get_bearer_token(self):
        return self.BEARER + self.get_token(self)

    # used for development
    def print_bearer_token(self):
        print(self.get_bearer_token())

    # supporter method
    def set_and_return_header(self):
        bearer_token = self.get_bearer_token(self)
        print(bearer_token)
        self.header = {'Content-type': 'application/json-patch+json', 'accept':'text/plain',
                       "Authorization" : bearer_token}
        return self.header

    @staticmethod
    def load_json_from_file(my_file_name):
        json_body = {}
        file_name = my_file_name
        with open (file_name, 'r') as jfile:
            file_read =  jfile.read()
        json_body = json.loads(file_read)
        print(json_body)
        return json_body

    @classmethod
    def create_send_post(self):
        self.body = self.load_json_from_file('sync1_tu_sample_request.json')
        self.header = self.set_and_return_header(self)

        self.credit_response =  requests.post(self.preview_credit_url,
                                             headers= self.header, json= self.body)

        print(self.credit_response.status_code)
        print(self.credit_response.url)






if __name__ == '__main__':
    p = Post()
    #p.log_in()
    #p.print_bearer_token()
    p.create_send_post()