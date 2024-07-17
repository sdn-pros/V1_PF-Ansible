from cvprac.cvp_client import CvpClient
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp = "www.arista.io"
cvp_user = "ansible"
cvaas_token = "" # Pulled this out as it's not encrypted
client = CvpClient()

client.connect([cvp], cvp_user, '', is_cvaas=True, cvaas_token=cvp_token)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)


configlets = client.api.get_configlets(start=0,end=0)

for item in configlets['data']:
    file = open(directory+'/'+item['name']+'.cfg','w')
    file.write(item['config'])
    file.close()