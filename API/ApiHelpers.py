import json
import requests
import time



class ApiHelpers:


    def write_resp_to_file(self, response_body):
        file_used = 'response1'
        file_name = file_used.strip() + str(time.process_time()).replace(".", "") + '.json'
        with open(file_name, 'w') as file1:
            # file1.write(json.dumps(response_body, indent=4, sort_keys=True))
            #file1.write(json.dumps(resp_dict, indent=4, sort_keys=True))
            file1.write(response_body)

    def import_json(self, file_name):
        json_file_name = file_name
        json_post_body = None
        with open(json_file_name, 'r') as js:
            json_string = js
            json_post_body = json.load(json_string)
            return json_post_body
