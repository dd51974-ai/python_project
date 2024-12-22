import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(data[:5]) #show first three