import requests


sess = requests.Session()
payload = {'page': 4, 'count': 50}
payload_post = {'username':'user1', }
r = sess.get('https://httpbin.org/get', params=payload)
r2 = sess.post()

print(r.text)
#print(dir(r))
#print(help(r))