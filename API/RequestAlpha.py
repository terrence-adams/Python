from BaseClass import ApiRequest
from BaseClass import ApiResponse
import requests
import json
import io
import time
import xml.etree.ElementTree as ET


class RequestAlpha:
    file_name = None
    json_post_body = {}
    preview_credit_url = 'https://preview.sync1creditservices.com/api/Credit'
    preview_login_url = 'https://preview.sync1creditservices.com/api/Login'
    login_request_session =  requests.session()
    token = ''
    header = {'Content-type': 'application/json-patch+json', 'accept': 'text/plain'}
    body = json= {'username': 'sync1@cuanswers.com', 'password': 'Testsync1'}


    def __init__(self):
        pass

# The intent is to pass in an IO object as the file object to open, but it may not be necessary
  #  def write_to_string(self):
   #     a = io.StringIO()
    #    with open(a, 'w') as my_string:
     #       my_string.write("Hello my world!")
      #      print(a)

    # loads from json file, returns a string which is then coverted into a python dict
    def import_json(self):
        #self.file_name = file_name
        with open('C:\Repo\Python\API\JsonFiles\sync1_tu_sample_request.json', 'r') as js:
            json_string = js

            self.json_post_body = json.load(json_string)
            #print(json_string)

        #print(self.json_post_body.items())

    def log_in(self):

        resp = self.login_request_session.post(
            self.preview_login_url, headers=self.header, json=self.body)
        login_dict = json.loads(resp.text)
        self.token = 'bearer ' + login_dict['token']['access_token']
        #print(self.token)
        return self.token

    def post_credit_to_credit_services(self):
        my_token = self.log_in()
        self.import_json()
        self.header.update({'authorization' : self.token})
        resp = requests.post(self.preview_credit_url, headers= self.header, json= self.json_post_body)
        print(resp.status_code)
        self.write_resp_to_file(resp.json())
        time.sleep(2)

    def create_multiple_submissions(self, i=1):
        for x in range(1, i + 1):
            self.post_credit_to_credit_services()

    """
    This method needs to be defined with a pattern for file naming convention
    But it writes a json file to the local directory which can then be imported.
    This will allow the recording of request responses for testing apis.

    """

    def write_resp_to_file(self, response_body):
        file_name = 'sync1_tu_sample_request.json' + str(time.process_time()).replace(".", "") + '.json'
        with open(file_name, 'w') as file1:
            # file1.write(json.dumps(response_body, indent=4, sort_keys=True))
            file1.write(json.dumps(response_body, indent=4, sort_keys=True))


    #looping through and exploring the xml for symitar
    def import_xml(self):
        tree = ET.parse('XMLFiles/memberlookup.xml')
        root = tree.getroot()

        #print(ET.dump(tree))
        
        for t in tree.iter():
            print(t)
        #print(tree['SSN'])
        print("_" * 102)

        for t in root.itertext():
            if t == None:
                pass

            print(t.strip())

        for e in root:
            print(e)
            for f in e:
                print(f)
                for g in f:
                    print(g)
                    for h in g:
                        print(h.attrib)
                        for i in h:
                            print(i)
                            for j in i:
                                print(j.text)





if __name__ == '__main__':
    reqA = RequestAlpha()
    #reqA.create_multiple_submissions(3)
    reqA.import_xml()
