import pandas as pd

dataFile = pd.read_csv("worldWordReduced.csv")

words = [u'korea', u'north', u'police', u'world', u'people', u'china', u'government', u'years', u'u.s', u'man', u'snowden', u'women', u'president', u'turkey', u'war', u'country', u'uk', u'death', u'south', u'amp', u'attack', u'russia', u'year', u'woman', u'internet', u'protests', u'law', u'news', u'%', u'canada', u'children', u'court', u'india', u'minister', u'secret', u'japan', u'un', u'new', u'girl', u'pope', u'!', u'israel', u'rights', u'american', u'syria', u'nsa', u'dead', u'men', u'gay', u'million', u'calls', u'thousands', u'bank', u'protest', u'ban', u'state', u'prison', u'muslim', u'rape', u'protesters', u'time', u'use', u'human', u'surveillance', u'europe', u'church', u'kim', u'bill', u'end', u'iran', u'data', u'group', u'germany', u'drugs', u'[', u'putin', u'drug', u'report', u']', u'bbc', u'edward', u'wikileaks', u'times', u'party', u'obama', u'child', u'australia', u'officials', u'tax', u'pay', u'week', u'shot', u'france', u'help', u'case', u'money', u'parliament', u'days', u'stop', u'get', u'pakistan', u'assange', u'brazil', u'media', u'security', u'google', u'egypt', u'eu', u'companies', u'united', u'girls', u'evidence', u'face', u'life', u'weapons', u'sex', u'jail', u'london', u'want', u'ecuador', u'acta', u'saudi', u'marriage', u'video', u'oil', u'gas', u'day', u'rebels', u'facebook', u'vatican', u'home', u'erdogan', u'warns', u'city', u'america', u'britain', u'states', u'gets', u'hong', u'set', u'show', u'arrest', u'call', u'system', u'access', u'intelligence', u'suicide', u'school', u'fire', u'pm', u'support', u'kong', u'countries', u'official', u'moscow', u'online', u'threatens', u'square', u'millions', u'dies', u'kill', u'run', u'daughter', u'forces', u'asylum', u'israeli', u'way', u'workers', u'company', u'plans', u'strike', u'leader', u'streets', u'program', u'control', u'percent']

count = -1
for x in dataFile["nouns"]:
  count +=1
  x = x.split()
  for word in x:
    if word in words:
      column = word + str(1)
      dataFile[column][count] = 1

dataFile = dataFile.fillna(0)

# for x in words:
# 
# 
dataFile.to_csv("doneReduced.csv")