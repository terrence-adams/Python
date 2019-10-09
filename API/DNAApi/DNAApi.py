import requests


class DNAApi:

    def __init__(self):
        self.DNA_saf_token = ''
        self.DNA_user_id = 'JSYNC1'
        self.DNA_password = 'sync1@DNA'
        self.DNA_device_id = ''
        self.DNA_product_definition_code = 'SAF2006'  # this is generally static and this value is only for the test env
        self.DNA_environment_id = 'PRODUCTION'  # for test environment purposes
        self.DNA_url = ' https://capidev.opensolutions.com:20001/SAF/ProductIntegration/ProductIntegration.asmx'
