# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv")
netflix_subset = netflix_df[netflix_df["type"] != 'TV Show']
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
short_movies = netflix_movies[netflix_movies["duration"] < 60]

colors = []
for lab, row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append("blue")
    elif row["genre"] == "Documentaries":
        colors.append("red")
    elif row["genre"] == "Stand-Up":
        colors.append("yellow")
    else:
        colors.append("gray")
# netflix_movies["color"] = colors

fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.release_year,netflix_movies.duration,c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.show()
