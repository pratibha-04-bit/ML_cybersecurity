import requests

url = "https://www.virustotal.com/api/v3/urls/aHR0cDovLzA1eXpiLXVwcXMudXM"

headers = {
    "accept": "application/json",
    "x-apikey": ""
}

response = requests.get(url, headers=headers)

print(response.text)
