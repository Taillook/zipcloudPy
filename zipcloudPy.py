import json
import sys
import requests

def main(zipcode):
    url = "http://zipcloud.ibsnet.co.jp/api/search"
    param = {"zipcode": zipcode}

    res = requests.get(url, params=param)
    address = json.loads(res.text)["results"][0]

    print(address["address1"] + address["address2"] + address["address3"])

main(sys.argv[1])
