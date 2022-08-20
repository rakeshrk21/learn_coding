from sre_constants import SUCCESS
from textwrap import indent
from urllib.error import HTTPError
import requests
import json
import logging
import http.client
import time
import csv

def getToken():
    username = '01aef45c-1fe2-4e11-8cf9-e15ad70ee217'
    password = 'D7E5quFaW5T5FvXR'
    url = 'https://login-dev.ultipro.com/v2/oauth2/us_internal/access_token'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'client_credentials', 'scope': 'openid profile'}
    r = requests.post(url, auth=(username, password), headers=headers, data=payload )
    # print(r.status_code)
    # print(json.dumps(r.json(), indent=2))
    return r.json()['token_type']+ ' ' + r.json()['access_token']
    
    
def deleteFeatureData(tenantId, token, date):
    http.client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    erroredFile = open("errored_tenants", "a")
    successFile = open("successful_tenants", "a")
    
    try:
        url = "https://performance-tenant-restore-cmd.continuous-performance-psr.dlas1.ucloud.int/talent/v1/tenant-restore/tenants/" + tenantId
        headers = {'content-type': 'application/json', 'x-tenant': tenantId, 'Authorization': token, 'current-user-id': '00000000-0000-0000-0000-000000000000'}
        params = { 'featureDataOnly': 'true', 'featureDataCreatedAtOrBefore': date, 'dataCountDisabled': 'true', 'fastDomainEventsDelete': 'true' }
        response = requests.delete(url=url, params=params, headers=headers, verify=False)
        response.raise_for_status
        jsonResponse = response.json()
        if response.status_code == 202:
            successFile.write(f'Tenant {tenantId} was processed successfully')
            successFile.write('\n')
            successFile.close
        return jsonResponse['requestId']
 
    except HTTPError as http_err:
        print(f'Http error occured: {http_err}')
            
    except Exception as exception:
        print(f'Other error occured: {exception}')
        erroredFile.write(f'Processing of tenant errored {tenantId}: {exception}')
        erroredFile.write('\n')
        erroredFile.close()
        

request_list = []
log = open("log.csv", 'a')       
with open("/Users/rakeshra/Developer/PerfDev/learn_python/data_parsing/homepage.csv", 'r') as infile:
    reader = csv.reader(infile)
    for line in reader:
        tenantId = line[0]
        token = getToken()
        date = '2022-07-15T21:09:12Z'
        requestId = deleteFeatureData(tenantId, token, date)
        request_list.append(requestId)
        print(f"Feature data deletion in progress for tenantId {tenantId} and requestId is {requestId}")
        log.write(f"Feature data deletion in progress for tenantId {tenantId} and requestId is {requestId}")
        log.write("\n")
        time.sleep(30)

print(request_list)
log.write(request_list)
log.close()
