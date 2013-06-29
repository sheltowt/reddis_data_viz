import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/RedditInsightWords.csv")

subreddits = ["Minecraft", "science", "leagueoflegends", "trees", "nsfw"]

data = data[[isinstance(x, basestring) for x in data["subreddit"]]]

count = 0
for subreddit in subreddits:
# 	if isinstance(subreddit, basestring):
	count = data[[x.startswith(subreddit) for x in data["subreddit"]]]
	count.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/" + subreddit + "words" +".csv")