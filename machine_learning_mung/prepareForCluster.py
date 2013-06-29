import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/preppedData/doneReduced.csv")

reducedData = data.drop(["domain", "subreddit", "title", "score", "downs", "permalink", "name", "created", "created_utc", "ups", "num_comments", "words", "verbs", "nouns", "year", "tm_min", "tm_mday", "day_week", "hour_day", "month", "tm_sec", "tm_yday"], axis=1)

reducedData.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/preppedData/newsCluster.csv")