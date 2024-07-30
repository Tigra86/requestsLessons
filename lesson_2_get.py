import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    # url="https://petstore.swagger.io/v2/store/inventory",
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    # auth=HTTPBasicAuth("username", "password"),
    headers={
        "api-key": "special-key"
    },
    params={
        "status": "available"
    }
    # verify=False
)
# print(response.status_code)
#
# response = response.json()
#
# print(response)
# print(response["sold"])

print(response.json())
