import requests
from datetime import datetime

from plotly.graph_objs import Bar
from plotly import offline


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
titles, links, comments_total, source_urls = [], [], [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    title = response_dict['title']
    article_url = f"http://news.ycombinator.com/item?id={submission_id}"
    link = f"<a href='{article_url}'>{title}</a>\t"
    try:
        comments = response_dict['descendants']
    except KeyError:
        comments = 0
    source_url = response_dict['url']
    titles.append(title)
    links.append(link)
    comments_total.append(comments)
    source_urls.append(source_url)

today = datetime.today().strftime('%Y-%m-%d')
data = [{
    'type': 'bar',
    'orientation': 'h',
    'y': links,
    'x': comments_total,
    'hovertext': source_urls,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
    'opacity': 0.6,
    }]

my_layout = {
    'title': f'Top 30 Articles on Hacker-News on {today}',
    'titlefont': {'size': 28},
    'yaxis': {
        'title': 'Descending Rank',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        'automargin': True,
        'autorange': 'reversed'
        },
    'xaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='top30_hn.html')
