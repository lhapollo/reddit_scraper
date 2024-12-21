import praw
import pandas as pd
import json

with open("config.json") as f:
    config = json.load(f)

#connecting Python to Reddit with PRAW
reddit_readonly = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"],
)

# accessing a subreddit and extracting basic info. 
subreddit = reddit_readonly.subreddit("TheWeeknd") 

print("Subreddit: ", subreddit.display_name)
print("Title:", subreddit.title)
print("Description", subreddit.description)

#Fetching top 10 posts from a subreddit
subreddit = reddit_readonly.subreddit("AITAH")

for post in subreddit.top(limit=10):
    print(post.title)
    print()

# Saving top posts from a subreddit into a pandas data frame.
subreddit = reddit_readonly.subreddit("uwaterloo")
posts = subreddit.top(time_filter='month')

posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [], "Total Comments": [], "Post URL": []}

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)

top_posts.to_csv("top_posts.csv", index=True)
