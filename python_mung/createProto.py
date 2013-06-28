import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data/RedditInsight.csv")

outData = data[:10000]

outData.to_csv("prototype2.csv")