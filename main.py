import pandas as pd

df = pd.read_csv('bestsellers.csv')

print(df.head())        #this shows the first 5 rows in the spreadsheet
print(df.shape)         #shows the shape of the spreadsheet
print(df.columns)       #shows the column name in the spreadhseet
print(df.describe())    #summary statistic for each cooumn

#check and remove any duplicate rows
df.drop_duplicates(inplace=True)    

#Renaming Columns
df.rename(columns={"Name": "Title", "Year": "Publication Year",  #change name to title and
                   "User Rating": "Rating"}, inplace=True)       # so on

#Converting Data Types
df["Price"] = df["Price"].astype(float)

#Analyzing Authot Popularity
author_counts = df['Author'].value_counts()
print(author_counts)

#Average Rating by Genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#Exporting the Results to CSV File

author_counts.head(10).to_csv("top_authors.csv")

avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
