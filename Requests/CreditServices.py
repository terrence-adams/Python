import requests
import json


class CreditServices:
    login_url = 'https://dev.sync1creditservices.com/api/Login'
    preview_login_url = 'https://preview.sync1creditservices.com/api/Login'
    credit_url = 'https://dev.sync1creditservices.com/api/Credit'
    preview_credit_url = 'https://preview.sync1creditservices.com/api/Credit'
    BEARER = 'bearer '  # constant
    credit_response = None
    token = ''

    def __init__(self):

        self.login = None
        self.resp_dict = {}
        self.token = ''
        self.header = {}
        self.body = {}
        self.bearer_token = ''
        self.session = None


    def create_session(self):
        self.session = requests.Session()
        self.login = self.session.post(self.preview_login_url,
                                 headers={'Content-type': 'application/json-patch+json', 'accept': 'text/plain'},
                                 json={'username': 'sync1@cuanswers.com', 'password': 'Testsync1'})
        self.resp_dict = json.loads(self.login.text)
        self.token = self.resp_dict['token']['access_token']
        self.header = self.login.headers
        self.body = self.login.text
        #print(self.token)


    # used for development
    def log_in(self):
        print(self.login.headers)
        print(self.login.status_code)
        print(self.login.text)
        print(self.login.url)
        print(self.login.json())
        print(self.token)

    #supporter method
    def get_token(self):
        return self.token

    # supporter method
    def get_bearer_token(self):
        self.bearer_token = self.BEARER + self.get_token()
        return self.bearer_token

    # supporter method

    def set_and_return_header(self):
        bearer_token = self.get_bearer_token()

        self.header = {'Content-type': 'application/json-patch+json', 'accept':'text/plain',
                       "Authorization": bearer_token}
        print(self.header)
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


    def create_send_post(self):
        self.body = self.load_json_from_file('sync1_tu_sample_request.json')
        self.header = self.set_and_return_header()
        print(self.body)
        post_resp= cs.session.post(self.preview_credit_url, data=self.body, headers=self.header)
        print(post_resp.status_code)





if __name__ == '__main__':
    cs = CreditServices()
    cs.create_session()
    cs.create_send_post()

    #cs.create_send_post()
