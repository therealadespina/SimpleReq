import requests
import pprint

# responce = requests.post('https://httpbin.org/post', json={'login': 'admin', 'password': 'admin1'})

responce = requests.post('https://httpbin.org/post')

print(responce.status_code)

if responce.status_code == 200:
  r = responce.json()
  print(pprint.pprint(r))
  # print(type(r))
  # print(r.keys())
  # print(r['headers'])
  # print(r['json']['password']) 
else:
  print("Error")
