import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import *


def api_call():
    x = 0
    tailnet="yalindogusahin.github"
    api_key="tskey-api-kDAtcr6CNTRL-AHCbaiVopp7WXNTGzixSr7XAkCXRST3P"
        
    url = ('https://api.tailscale.com/api/v2/tailnet/{}/devices'.format(tailnet))

    response = requests.get(url, auth=HTTPBasicAuth(api_key,''))

    data = json.loads(response.text)
    data = data['devices']
    ip_addresses = []
    hostnames = []
    last_seen = []
    device = []
    y = []
    
    
    for i in data:
        if(data[x]['os'] == 'linux'):

            # Gets  IP addresses as list
            ip_addresses.append(data[x]['addresses'][0])

            # Gets Hostnames as list
            hostnames.append(data[x]['hostname'])

            
            last_seen.append(data[x]['lastSeen']) 
            
            device = list(zip(hostnames,ip_addresses))
            
            
        x = x+1
        
    # Last seen converted to date time format
    for i in last_seen:
        y.append(datetime.strptime(i,"%Y-%m-%dT%H:%M:%SZ"))
    
    return device

api_call()