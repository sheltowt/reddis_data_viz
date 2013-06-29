import pandas as pd
import nltk

subset = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/RedditInsight.csv")
subset["words"] = ""
subset["verbs"] = ""
subset["nouns"] = ""

desiredParts = ["NN", "NNP", "NNS", "NNPS", "VB", "VBD", "VBG", "VBP", "VBZ", "VBN", "JJ"]

nouns = ["NN", "NNP", "NNS", "NNPS"]
verbs = ["VB", "VBD", "VBG", "VBP", "VBZ", "VBN"]

count = -1
for title in subset["title"]:
  count += 1
  clean = []
  y = nltk.word_tokenize(title)
  y = [nltk.word_tokenize(a) for a in y]
  y = [nltk.pos_tag(a) for a in y]
  clean.append(y)
  goodWords = ''
  nounWords = ''
  verbWords = ''
  for x in clean:
    for word in x:
      print word
      if word[0][1] in desiredParts:
        print word[0][0]
        goodWords = goodWords + " " + word[0][0]
      if word[0][1] in nouns:
        print word[0][0]
        nounWords = nounWords + " " + word[0][0]
      if word[0][1] in verbs:
        print word[0][0]
        verbWords = verbWords + " " + word[0][0]
  subset["words"][count] = goodWords.lower()
  subset["verbs"][count] = verbWords.lower()
  subset["nouns"][count] = nounWords.lower()

subset.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/RedditInsightWords.csv") 