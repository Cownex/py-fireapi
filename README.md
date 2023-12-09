# Python FireAPI Client
Unofficial API client for the FireAPI from 24fire GmbH. <br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Installation
````shell
pip install python_fireapi
````

## Examples
### 1. List all VMs
````python
from python_fireapi import FireAPIClient

# Set the client and authenticate
client = FireAPIClient("api-key")

# Perform the Request
r = client.vm.list_all_vms()

# Print statuscode
print("Status Code: ", r.status_code)

# Print json
print(r.json())
````

Output:
```Status Code: 200```

````json
{
    "status": "success",
    "requestID": "a24effc3-b1d6-46a3-a49a-fe07734717ad",
    "message": "All vm data are listed below",
    "data": {
        "total_vms": 2,
        "total_stats": {
            "cores": 12,
            "mem": 3072,
            "disk": 20
        },
        "list": [
            {
                "vmid": 30071,
                "createDate": "2023-05-31T00:38:40.000Z",
                "node": "node09",
                "config": {
                    "cores": 10,
                    "mem": 1024,
                    "disk": 10
                }
            },
            {
                "vmid": 30074,
                "createDate": "2023-06-10T11:10:34.000Z",
                "node": "node09",
                "config": {
                    "cores": 2,
                    "mem": 2048,
                    "disk": 10
                }
            }
        ]
    }
}
````
