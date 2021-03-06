from flask import Flask
from flask import render_template
from flask import request
import feedparser


app = Flask(__name__)

RSS_FEEDS = {'bbc' : 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss' }


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    rss_url = RSS_FEEDS[publication]
    feed = feedparser.parse(rss_url)
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)