import pandas as pd
from collections import Counter
import json


subreddits = ["Minecraft", "science", "leagueoflegends", "trees", "nsfw"]


for subreddit in subreddits:
	cnt = Counter()
	data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/" + subreddit + "/" + subreddit + "words.csv")
	for sentence in data["nouns"]:
	  if isinstance(sentence, basestring):
	    print sentence
	    sentence = sentence.split()
	    for word in sentence:
	      print word
	      cnt[word] +=1
	
	print cnt
	
	columns = ['nouns', 'frequency']
	index = range(0, 10000)
	
	
	freq = pd.DataFrame(index=index, columns=columns)
	
	count = 0
	for word in cnt:
	  if count < 10000:
	    freq["nouns"][count] = word
	    freq["frequency"][count] = cnt[word]
	    count = count + 1
	
	freq.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/" + subreddit + "/" + subreddit + "frequencyLargeNouns.csv")
	
	freq = freq.sort_index(by='frequency', ascending=False) 
	
	f_new = open("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/" + subreddit + "/" + subreddit + "frequencyLargeNouns.json", 'w')
	
	d = [ 
	    dict([
	        (colname, row[i]) 
	        for i,colname in enumerate(freq.columns)
	    ])
	    for row in freq.values
	]
	
	f_new_stage = json.dumps(d)
	
	f_new.write(f_new_stage+'\n')