import requests
import plotly.express as px 

# Make an API call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars&per_page50&page=1"

headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# Process results
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete Results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
repo_names = [repo_dict["name"] for repo_dict in repo_dicts]
star_count = [repo_dict["stargazers_count"] for repo_dict in repo_dicts]
hover_data = [f"{repo_dict['name']}<br />{repo_dict['owner']['login']}<br />{repo_dict['description']}"for repo_dict in repo_dicts]
repo_links = [f"<a href = '{repo_dict['html_url']}' > {repo_dict['name']}</a>" for repo_dict in repo_dicts]

title = "Most-Starred Python Projects on GitHub"
labels = {"x":"Repository", "y":"Stars"}

fig = px.bar(
    x=repo_links,
    y=star_count,
    title=title,
    labels=labels,
    color=repo_names,
    color_continuous_scale="viridis",
    template="plotly_dark",
    hover_name=hover_data)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    legend_title_text="Repository Name",  # Change legend title
    legend=dict(
        font=dict(size=12, color="white"),  # Change legend font color and size
        bgcolor="black",                    # Background color
        bordercolor="white",                # Border color
        borderwidth=1,))

fig.update_traces(marker_opacity=0.6)
# In Plotly, a trace refers to a collection of data on a chart. 
# The update _traces() method can take a number of different arguments;

fig.show()