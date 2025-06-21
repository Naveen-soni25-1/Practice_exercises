import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/44314423.json"
r = requests.get(url)

print(f"Status Code: {r.status_code}")

response_dict = r.json()

response_string = json.dumps(response_dict, indent=4)
print(response_string)
#"descendants" tells us the number of comments the article has received 
# The key "kids" provides the IDs of all comments made directly in response to this submission