import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
print(response.json())
print(response.json()["iss_position"])
print(response.json()["iss_position"]["longitude"]) 