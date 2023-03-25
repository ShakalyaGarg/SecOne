import requests
import json

placeholder="ED24ED04B5D4A20B3F50FC088A455195C756D7B5315D1965E8C569472B43D939"
url = "https://www.virustotal.com/api/v3/files/" + placeholder

headers = {
    "accept": "application/json",
    "x-apikey": "4ab826c543206d45073f7f5fea0a5d5ed9eaf23a8b8e49b4190287a741287933"
}

response = requests.get(url, headers=headers)

print(response.text)
