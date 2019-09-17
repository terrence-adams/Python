import requests
__author__ = 'adam0954'



class Get:

    url = 'http://dev.sync1services.com/Version'

    def get_status(self):
        self.s = requests.Session()
        self.r = self.s.get(self.url)
        print(self.r.headers)



if __name__ == '__main__':
    g =  Get()
    g.get_status()



