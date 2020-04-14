import requests


class ApiResponse:

    def __init__(self, api_response = requests.Response()):
        self.response = api_response
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code
        self.response_url = self.response.url
        self.original_request = self.response.request
        self.response_headers = self.response.headers
        self.header_links = self.response.links
        print("Status code is %s" % self.response.status_code)
        print(self.response.reason)
        print("Url called is %s" % self.response.url)
        print("Response content: %s" % self.response.text)
