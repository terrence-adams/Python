import requests


class ApiRequest:

    def __init__(self, api_url=''):
        self.url = api_url
        self.session = requests.Session()
        self.header = {}
        self.data = {}
        self.token = ''
        self.json_body = {}
        self.xml_body = ""
