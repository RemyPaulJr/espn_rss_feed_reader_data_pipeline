import feedparser
import json

url = "https://www.espn.com/espn/rss/nba/news"
feed = feedparser.parse(url)

feed_dictionary = {
    "Feed Title": feed.feed.title,
    "Feed Link": feed.feed.link,
    "entries": []
}

for entry in feed.entries:
    entry_data = {
        'Title': entry.get('title','None'),
        'Published': entry.get('published','None'),
        'Author': entry.get('author','None'),
        'Summary': entry.get('summary','None'),
        'Link': entry.get('link','None')
    }

    feed_dictionary["entries"].append(entry_data)

with open("epsn_nba_news.json", "w") as json_file:
    json.dump(feed_dictionary, json_file, indent=4)

print("Successfully stored json file!")
    