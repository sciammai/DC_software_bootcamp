import requests
import json

from utils.auth import IntersightAuth
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'

#Alarms request (description)
url_alarms = f"{BASE_URL}/cond/Alarms"

try:
    response = requests.get(url_alarms, auth=auth).json()
    # print('Alarms description: ')
    for r in response['Results']:
        alarm_description = r['Description']
        # print(alarm_description)
except Exception as ex:
    print(ex)


#Summary physical infrastructures request (management mode, management IP, Name, CPUs, Cores, PowerState, Firmware, Model, Serial, License Tier)
url_spi = f"{BASE_URL}/compute/PhysicalSummaries"

try:
    response = requests.get(url_spi, auth=auth).json()
    for r in response['Results']:
        man_mode = r['ManagementMode']
        man_IP = r['MgmtIpAddress']
        name = r['Name']
        CPUs = r['NumCpus']
        cores = r['NumCpuCores']
        power_state = r['OperPowerState']
        firmware = r['Firmware']
        model = r['Model']
        serial = r['Serial']
        license_tier = r['SharedScope']
#        print('Management Mode: ' + str(man_mode) + '\n' + 'Management IP: ' + str(man_IP) + '\n' + 'Name: ' + str(name) + '\n' + 'CPUs: ' + str(CPUs) + '\n' + 'Cores: ' + str(cores) + '\n' + 'Power State: ' + str(power_state) + '\n' + 'Firmware: ' + str(firmware) + '\n' + 'Model: ' + str(model) + '\n' + 'Serial: ' + str(serial) + '\n' + 'License Tier: ' + str(license_tier))
except Exception as ex:
    print(ex)


#Compliance HCL request (OS vendor, OS Version)
url_HCL = f"{BASE_URL}/cond/HclStatuses"

try:
    response = requests.get(url_HCL, auth=auth).json()
    for r in response['Results']:
        OS_vendor = r['HclOsVendor']
        OS_version = r['HclOsVersion']
        # print('OS Vendor: ' + str(OS_vendor) + '\n' + 'OS Version: ' + str(OS_version))
except Exception as ex:
    print(ex)


#Kubernetes clusters running on this cluster request (names)
url_kub = f"{BASE_URL}/kubernetes/Clusters"

try:
    response = requests.get(url_kub, auth=auth).json()
    # print('Kubernetes clusters names: ')
    for r in response['Results']:
        k_name = r['Name']
        # print(k_name)
except Exception as ex:
    print(ex)


#Deployments running in kubernates cluster (number of deployments)
url_depl = f"{BASE_URL}/kubernetes/Deployments"

num = 0
try:
    response = requests.get(url_depl, auth=auth).json()
    for r in response["Results"]:
            num=num+1
    k_deployments = num
    # print(f"The number of the Kubernetes deployments is: " + str(k_deployments))
except Exception as ex:
    print(ex)
