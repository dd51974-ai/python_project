import requests

payload = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")