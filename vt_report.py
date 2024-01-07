import requests

url = "https://www.virustotal.com/api/v3/urls/aHR0cDovLzA1eXpiLXVwcXMudXM"

headers = {
    "accept": "application/json",
    "x-apikey": "982ce415cf8ef4cae0c948f2eb9dddd2cb68119f7a57d5e95c5af8b66f7dcde7"
}

response = requests.get(url, headers=headers)

print(response.text)