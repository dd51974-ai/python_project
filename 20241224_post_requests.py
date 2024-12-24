import requests
url = "https://reqres.in/api/users"
payload = {
    "name" : "Ai Tsujikawa",
    "job" : "Developer"
}

#sent data
response = requests.post(url, json=payload)
if response.status_code == 201:
    print("ユーザーが作成されました!")
    print(response.json())
else:
    print("エラー:",response.status_code)
