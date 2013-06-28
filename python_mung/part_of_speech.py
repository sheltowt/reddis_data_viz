import pandas as pd
import nltk

subset = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data_by_subreddit/funny/funny.csv")
subset["words"] = ""

count = -1
for title in subset["title"]:
  count += 1
  clean = []
  y = nltk.word_tokenize(title)
  y = [nltk.word_tokenize(a) for a in y]
  y = [nltk.pos_tag(a) for a in y]
  clean.append(y)
  goodWords = ''
  for x in clean:
  	if x[0][1] in ["NN", "NNP", "NNS", "NNPS", "VB", "VBD", "VBG", "VBP", "VBZ", "VBN", "JJ", "JJS", "JJR", "CC", "CD", "TO", "MD", "RB", "RBR", "RBS", "FW"]:
  	  goodWords = goodWords + x[0][0]
  subset["words"][count] = goodwords.lower()

subset.to_csv("/Users/williamshelton/Desktop/reddis_data_viz/data_by_subreddit/funny/funnyFiltered.csv") 