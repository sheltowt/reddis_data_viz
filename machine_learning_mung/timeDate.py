import pandas as pd
import datetime
import dateutil.parser
import time

oldFile = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/MLdataSetWorld.csv")

# taking a subset of dataset
# oldFile = oldFile[:1000]
oldFile["year"] = 0
oldFile["tm_min"] = 0
oldFile["tm_mday"] = 0
oldFile["day_week"] = 0
oldFile["hour_day"] = 0
oldFile["month"] = 0
oldFile["tm_sec"] = 0
oldFile["tm_yday"] = 0

count = -1
for x in oldFile["created_utc"]:
  count += 1
  try:
    z = time.gmtime(x)
    oldFile["year"][count] = z[0]
    oldFile["tm_mday"][count] = z[2]
    oldFile["day_week"][count] = z[6]
    oldFile["hour_day"][count] = z[3]
    oldFile["tm_min"][count] = z[4]
    oldFile["month"][count] = z[1]
    oldFile["tm_sec"][count] = z[5]
    oldFile["tm_yday"][count] = z[7]
    print z[6]
  except:
    pass
#     x = dateutil.parser.parse(x)
#     z = datetime.date.timetuple(x)
#     print z[6]
#     oldFile["day_week"][count] = z[6]
#     print x.hour
#     oldFile["hour_day"][count] = x.hour

  

print oldFile

oldFile.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/MLdataSetWorldTIMEALL.csv")