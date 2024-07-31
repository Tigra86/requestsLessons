import requests

"""
response = requests.put(
    url="https://jsonplaceholder.typicode.com/posts/1",
    json={
        "title": "TEST"
    }
)

print(response.json())
"""

response = requests.patch(
    url="https://jsonplaceholder.typicode.com/posts/2",
    json={
        "title": "Hello"
    }
)

print(response.json())
