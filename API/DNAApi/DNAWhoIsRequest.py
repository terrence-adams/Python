import requests
import json
from DNAApi import DNAApi
from ApiHelpers import ApiHelpers


class DNAWhoIsRequest:
    ah = ApiHelpers()

    def __init__(self):
        self.dna = DNAApi()
        self.session = requests.Session()

    def dna_auth_login(self):
        header_dict = {'Content-Type': 'application/json'}
        dna_url = self.dna.DNA_url
        data_body = {'ProdDefCd': 'SAF2006', 'ProductEnvironment': 'Production',
                     'NetworkNode': 'DEMO'}
        auth_body = {'UserId': 'JSYNC1', 'Password' : 'sync1@DNA'}
        response = self.session.post(dna_url, headers=header_dict, data=data_body,
                                     auth=(self.dna.DNA_user_id, self.dna.DNA_password))
        response.raise_for_status()








if __name__ == '__main__':
    dna1 = DNAWhoIsRequest()
    dna1.dna_auth_login()
