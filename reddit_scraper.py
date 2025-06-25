import praw
import json
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="startup_chatbot/0.1",
)

def fetch_posts(subreddit_name="startups", limit=500):
    subreddit = reddit.subreddit(subreddit_name)
    data = []
    for submission in subreddit.hot(limit=limit):
        post_data = {
            "title": submission.title,
            "selftext": submission.selftext,
            "comments": [comment.body for comment in submission.comments if hasattr(comment, 'body')]
        }
        data.append(post_data)
    with open("reddit_data.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    fetch_posts()