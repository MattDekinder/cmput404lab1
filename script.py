import requests
r = requests.get("https://raw.githubusercontent.com/MattDekinder/cmput404lab1/master/script.py")

print r.status_code
print r.text
