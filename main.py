from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme_old():
    url = "https://meme-api.com"
    response = json.loads(requests.request("GET", url).text)
    meme = response["preview"][-2]
    subreddit = response['subreddit']
    return meme, subreddit
def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        meme_url = data.get("url", "Default URL")  # Get the direct URL of the meme
        subreddit = data.get('subreddit', 'Unknown Subreddit')  # Get the subreddit
    except requests.RequestException as e:
        print(f"Error fetching meme: {e}")
        meme_url, subreddit = "Error", "Error"
    return meme_url, subreddit

@app.route("/")
def index():
    meme, subreddit = get_meme()
    return render_template("index.html", meme=meme, subreddit=subreddit)
