import requests

"""
response = requests.post(
    url="https://petstore.swagger.io/v2/pet",
    headers={
        "api-key": "special-key"
    },
    json={
        "id": 100,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "Sky",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "dogs"
            }
          ],
          "status": "available"
    }
)
print(response.json())

get_pet_by_id = requests.get(
    url="https://petstore.swagger.io/v2/pet/100",
    headers={
        "api-key": "special-key"
    }
)

print(get_pet_by_id.json())
"""
response = requests.post(
    url="https://petstore.swagger.io/v2/pet/100/uploadImage",
    headers={
        "api-key": "special-key"
    },
    files={
        "file": ("example.jpg", open("example.jpg", "rb"), "image/jpeg")
    }
)

print(response.status_code)
print(response.json())
