import requests

# Make an API call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars"
headers = {
    "Accept": "application/vnd.github.v3+json"
}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# Process results
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete Results: {not response_dict['incomplete_results']}")

# Exploring the repository
repo_dicts = response_dict["items"]
print(f"Repositories Returned: {len(repo_dicts)}")

print("Selected inforation about the Repositories:")
num_option = ["name", "full_name", "description", "html_url", "stargazers_count","created_at","updated_at"]
for repo_dict in repo_dicts:
    for word in num_option:
        print(f"{word.replace("_"," ").title()}: {repo_dict[word]}")
    print("\n")
