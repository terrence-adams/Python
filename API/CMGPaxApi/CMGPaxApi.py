import json
import requests
from ApiHelpers import ApiHelpers
import time

class CMGPaxApi:
    helpers = ApiHelpers()


    def __init__(self):
        self.headers = {'ExternalTrackingNumber': '12', 'X-VendorID' : 'Sync1', 'Authentication-UserName':'SA-SYNC1-SYSTEMS-P',
                        'X-CreditUnionID' : '04225030', 'X-UserID' : 'Terrenceadams',
                        'Authentication-Password' : 'NyKq29uafdGz', 'X-IBM-Client-ID' : 'dec6953a-67a1-49f9-8809-9fd804df027f', 'Content-Type': 'application/json'}
        self.body = {}
        self.url = 'https://apigateway.cunamutual.com/cmfg/pre-prod/lendingproducts/v1.0/LoanCalculator/Quotes'
        self.session = requests.Session()
        self.json_file_name = ''

    def get_json_file_name(self):
        #temp_name = input('What is the file name?: ').strip()
        #if type(temp_name) == type(str):
        self.json_file_name = 'cmgpaxbody1.json'


    def post_to_api(self):
        self.body = self.helpers.import_json(self.json_file_name)
        resp = self.session.post(self.url,auth=('SA-SYNC1-SYSTEMS-P', 'NyKq29uafdGz'), headers=self.headers,json=self.body)
        print(resp.status_code)
        print(resp.text)
        self.helpers.write_resp_to_file(resp.text)



if __name__ == '__main__':
    cmg = CMGPaxApi()
    cmg.get_json_file_name()
    cmg.post_to_api()



