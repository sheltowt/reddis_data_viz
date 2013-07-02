import pandas as pd

subreddits = ["AdviceAnimals", "aww", "funny", "gamming", "gifs", "leagueoflegend", "Minecraft", "nsfw", "pics", "politics", "science", "technology", "todayilearned", "trees", "videos", "WTF"]

# for subreddit in subreddits:

# subreddit = "AdviceAnimals"

for subreddit in subreddits:
	data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/clusteredSubreddits/scoredData/" + subreddit + "_train_score_all.csv")
	pieces = [data["kmeans"], data["nouns"]]
	data = pd.concat(pieces, axis=1)
	# reducedData = reducedData.applymap(lambda x: 0 if str(x) == '' else x)
	count = 1
	while count < 11:
	# 	if isinstance(subreddit, basestring):
	# 	subset = data[[x.startswith(count) for x in data["kmeans"]]]
	  subset = data[data["kmeans"] == count]
	  subset.to_csv(subreddit + "/cluster" + str(count) +".csv")
	  count +=1

	data.to_csv(subreddit + "data" + ".csv")

