import pandas as pd
from collections import Counter
import json

cnt = Counter()

# import large file
# filter by part of speech
# segment by subreddit
# save csvs and json to subfiles

data = read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/RedditInsightWords.csv")

subreddits = ["pics", "funny", "politics", "videos", "technology", "worldnews", "aww", "WTF", "gaming", "gifs", "todayilearned", "AdviceAnimals"]

count = 0
for subreddit in subreddits:

	count = data[[x.startswith(subreddit) for x in data["subreddit"]]]
	count.to_csv("/Users/williamshelton/Desktop/reddis_data_viz/data_by_subreddit/" + subreddit + ".csv")
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

freq.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funnyFilteredFrequency.csv")

freq = freq.sort_index(by='frequency', ascending=False) 

f_new = open('/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/funny/funnyFilteredFrequency.json', 'w')

d = [ 
    dict([
        (colname, row[i]) 
        for i,colname in enumerate(freq.columns)
    ])
    for row in freq.values
]

f_new_stage = json.dumps(d)

f_new.write(f_new_stage+'\n')