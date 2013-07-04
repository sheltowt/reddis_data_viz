import pandas as pd

clusters = pd.read_csv("newCluster_10.csv")
original = pd.read_csv("worldWordReduced.csv")

pieces = [clusters["kmeans"], original["nouns"]]

concatenated = pd.concat(pieces, axis=1)

count = 1
while count < 10:
# 	if isinstance(subreddit, basestring):
# 	subset = data[[x.startswith(count) for x in data["kmeans"]]]
  subset = concatenated[concatenated["kmeans"] == count]
  subset.to_csv("clusters/cluster" + str(count) +".csv")
  count +=1