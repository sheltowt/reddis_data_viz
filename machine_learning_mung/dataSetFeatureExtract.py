import pandas as pd

oldFile = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data_by_subreddit/worldnews/worldnewswords.csv")

newFile = oldFile.drop(["banned_by", "selftext_html", "selftext", "likes", "link_flair_text", "id", "clicked", "media", "approved_by", "over_18", "hidden", "thumbnail", "subreddit_id", "edited", "link_flair_css_class", "author_flair_css_class", "saved", "is_self", "url", "author_flair_text", "author", "num_reports", "distinguished", "_id", "__v", "Unnamed: 0"], axis=1)

newFile.to_csv("/Users/williamshelton/Desktop/reddis_data_viz2/data/MLdataSetWorld.csv")