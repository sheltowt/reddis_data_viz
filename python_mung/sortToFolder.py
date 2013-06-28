import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data/prototype2.csv")

subreddits = ["pics", "funny", "politics", "videos", "technology", "worldnews", "aww", "WTF", "gaming", "gifs", "todayilearned", "AdviceAnimals"]

count = 0
for subreddit in subreddits:
	count = data[[x.startswith(subreddit) for x in data["subreddit"]]]
	count.to_csv("/Users/williamshelton/Desktop/reddis_data_viz/data_by_subreddit/" + subreddit + ".csv")
