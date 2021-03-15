import requests
import json

from utils.auth import IntersightAuth
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'

#NTP Policies request
url_ntp = f"{BASE_URL}/ntp/Policies"

try:
    response = requests.get(url_ntp, auth=auth).json()
    for r in response['Results']:
        print("The name of the concrete policy is " + r['Name'] + " and the IP address of the NTP server is " + r['NtpServers'][0])
    print(json.dumps(response, indent=4))
except Exception as ex:
    print(ex)