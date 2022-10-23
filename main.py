from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme = response["preview"][-2]
    subreddit = response['subreddit']
    return meme, subreddit

@app.route("/")
def index():
    meme, subreddit = get_meme()
    return render_template("index.html")

app.run(host="0.0.0.0", port=80)