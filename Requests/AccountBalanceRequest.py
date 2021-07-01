import json
import requests

url = "https://api-sandbox.sebgroup.com/ais/v6/identified2/accounts/5a59028c-e757-4f22-b88c-3ba90573383c/balances"

headers = {
    'Accept': 'application/json',
    'X-Request-ID': '24848c2c-15b9-46e6-a6a6-e68e42727aa9',
    'PSU-IP-Address': '129.178.88.88',
    'Authorization': 'Bearer mviOec9YH6u6YNUB05j4',
    'Cookie': 'C0WNET=77b97511-60dc-4ec7-a30b-29cb2bba34a0; AMWEBJCT!%2Fmga!JSESSIONID=0000F53HcDLyrSgxfjqOXKQCZvo:938ed943-3c20-4801-ace0-52dd1dd31f86; PD-SESSION-ID=1_4_1_CbJOrE7hxWz22nqGObKz4jfSVo2Un4rTMr7fCOaYJusbe66J; PGNET=7a2efed9-60dd-4973-a235-f03518dcac86; TS01136fc4=0107224bed70c30cf2a8c2726b0b1f20e02242c51d29b8f7fff4dff1ee45f994cdae5420e0390b98bbc6c01de7be7a0018afd1940e; TS018787d1=0107224bed4d939241909a766fa271b066eb277d22e00f0ca914ae43033577b6771af34b348e4caff80c89a5c5e2bb7abdbc860609'
}

response = requests.request("GET", url, headers=headers)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))