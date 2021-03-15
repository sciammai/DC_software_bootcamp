import requests
import json

from utils.auth import get_authenticated_aci_session
from env import config

aci_session = get_authenticated_aci_session(config['ACI_USER'], config['ACI_PASSWORD'], config['ACI_BASE_URL'])

if aci_session is not None:
    print("ACI access verified")
else:
    print("Failed to verify access to ACI.")

BASE_URL = config['ACI_BASE_URL']
url = f"{BASE_URL}/api/class/fabricHealthTotal.json"

try:
    response = requests.get(url, auth=aci_session).json()
    print(json.dumps(response, indent=4))
except Exception as ex:
    print(ex)


# with open("health.txt", 'w') as output:
#     for row in health:
#         output.write(str(row) + '\n')
