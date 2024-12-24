import requests

#get date
response = requests.get("https://jsonplaceholder.typicode.com/albums")
if response.status_code == 200:
    print("データ取得成功!")
    print(response.json()[:3]) #print first three
else:
    print("エラー:",response.status_code)