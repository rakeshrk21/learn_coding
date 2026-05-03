import json

json_data_age = '''
{
    "rakesh": 47,
    "asha": 38,
    "shiv": 8,
    "neel": 5
}
'''

di = json.loads(json_data_age) #returns a dictionary object
print(isinstance(di, dict))

for key, val in di.items():
    print(key, val)

json_data = '''
{
    "name": "NetworkConfig",
    "servers": [
        {
            "name": "Server1",
            "ip_address": "192.168.1.10"
        },
        {
            "name": "Server2",
            "ip_address": "10.0.0.25"
        }
    ],
    "backup_servers": [
        {
            "name": "BackupServer1",
            "ip_address": "172.16.0.5"
        },
        {
            "name": "BackupServer2",
            "ip_address": "192.168.1.20"
        }
    ],
    "gateway": "192.168.1.1"
}
'''

def find_ips(json):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = []

