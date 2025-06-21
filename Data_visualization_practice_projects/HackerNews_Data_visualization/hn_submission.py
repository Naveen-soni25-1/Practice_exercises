from operator import itemgetter

import requests

# Make an API call and check response.
url =  "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []

# loop through the submission ids
for submission_id in submission_ids[:10]:
    url =  f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    responsive_dict = r.json()
    print(f"{submission_id}\tStatus: {r.status_code}")

    submission_dict = {
        'title': responsive_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': responsive_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link : {submission_dict['hn_link']}")
    print(f"Comments : {submission_dict['comments']}")