import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data/prototype.csv")

data2 = data[[x.startswith("pics") for x in data["subreddit"]]]

for x in data2["subreddit"]:
  print x
    
