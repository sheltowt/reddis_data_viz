import pandas as pd
import nltk

subset = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funny.csv")
subset["words"] = ""

desiredParts = ["NN", "NNP", "NNS", "NNPS", "VB", "VBD", "VBG", "VBP", "VBZ", "VBN", "JJ", "JJS", "JJR", "RB", "RBR", "RBS"]

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
    for word in x:
      print word
      if word[0][1] in desiredParts:
        print word[0][0]
        goodWords = goodWords + " " + word[0][0]
  subset["words"][count] = goodWords.lower()

subset.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funnyFiltered.csv") 