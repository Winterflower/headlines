from flask import Flask
from flask import render_template
import feedparser


app = Flask(__name__)

RSS_FEEDS = {'irunfar' : 'http://feeds.feedburner.com/irunfar/wAAy?format=xml',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss' }


@app.route("/")
@app.route("/<publication>")
def get_news(publication="irunfar"):
    rss_url = RSS_FEEDS[publication]
    feed = feedparser.parse(rss_url)
    first_article = feed['entries'][0]
    title = first_article.get("title")
    published = first_article.get("published")
    summary = first_article.get("summary")
    return render_template("home.html", title=title, published=published, summary=summary)

if __name__ == "__main__":
    app.run(port=5000, debug=True)