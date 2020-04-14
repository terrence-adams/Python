import json
import requests
import time
from xml.etree import ElementTree as ET


class ApiHelpers:

    def write_resp_to_file(self, response_body):
        file_used = 'response1'
        file_name = file_used.strip() + str(time.process_time()).replace(".", "") + '.json'
        with open(file_name, 'w') as file1:
            # file1.write(json.dumps(response_body, indent=4, sort_keys=True))
            # file1.write(json.dumps(resp_dict, indent=4, sort_keys=True))
            file1.write(response_body)

    def import_json(self, file_name):
        json_file_name = file_name
        json_post_body = None
        with open(json_file_name, 'r') as js:
            json_string = js
            json_post_body = json.load(json_string)
            return json_post_body

        #  used to prevent non private attributes in
    def print_non_private_attribs(self, type_of_a: object()):

        for i in [a for a in dir(type_of_a) if not a.startswith('__')]:  # removes all attributes that are intenral
            print(i)

    def import_xml(self, xml_path):
        tree = ET.parse(xml_path)



if __name__ == '__main__':
    ah = ApiHelpers()
    x = 0
    ah.print_non_private_attribs(x)  # example of function to demonstrate available functions for types passed in
