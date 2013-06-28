import pandas as pd
from collections import Counter

cnt = Counter()

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funnyFiltered.csv")

for sentence in data["words"]:
  sentence = sentence.split()
  for word in sentence:
    cnt[word] +=1

print cnt

columns = ['word', 'frequency']
index = range(0, 1400)


freq = pd.DataFrame(index=index, columns=columns)

count = 0
for word in cnt:
  if cnt[word] > 10:
    freq["word"][count] = word
    freq["frequency"][count] = cnt[word]
    count = count + 1

freq.to_json("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funnyFilteredFrequency.json")
