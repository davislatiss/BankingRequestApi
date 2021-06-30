import requests
import json

url = "https://api-sandbox.sebgroup.com/ais/v6/identified2/accounts/5a59028c-e757-4f22-b88c-3ba90573383c?withBalance=true"


headers = {
    'Accept': 'application/json',
    'X-Request-ID': '41151176-1540-4da2-a2bb-3aaffec7eb99',
    'PSU-IP-Address': '129.178.88.88',
    'Cookie': 'C0WNET=77b97511-60dc-4ec7-a30b-29cb2bba34a0; TS0111c347=0107224bedea62dc62f59d862fde90c6f01f56f68a26a0fedef76dc6e1ab55cba483a0d8c45ec547a60dd9a15559c1ec0ffb001aae; AMWEBJCT!%2Fmga!JSESSIONID=0000II33GVlcgFrwWYZobgRYmIy:938ed943-3c20-4801-ace0-52dd1dd31f86; PD-SESSION-ID=1_4_1_DdHDBMnT-BYpeeC4IT9S0IiwsC7qzbOBD0UmxCgS99IMMrra; PGNET=77b97511-60dc-4ec7-a30b-29cb2bba34a0; TS01136fc4=0107224bed0c55a73fe49e4bdb7b3bf6675c2e6d18e855b5e9417c33bf0b157b8ac58951f65462ed41fee8e81701dda5e9d9c5e50a; TS018787d1=0107224bed94c812f71a30bc2701042242fb7b7ae40b44654ca6072a0187d9aa7236aae4fd6a1b6128efe18b1fdf46153540dedbec'
}

response = requests.request("GET", url, headers=headers)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))