import pandas as pd
import nltk

subset = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data_by_subreddit/funny/funny.csv")

for title in subset["title"]:
  clean = []
  y = nltk.word_tokenize(title)
  y = [nltk.word_tokenize(a) for a in y]
  y = [nltk.pos_tag(a) for a in y]
  clean.append(y)
  print clean