# **Netflix Movies Analysis**

## **Objective 1: Netflix Movies Analysis in 1990s**
The primary goal of this project is to perform exploratory data analysis (EDA) on Netflix movies released in the 1990s, focusing on:
1. Determining the most frequent movie duration in the 1990s.
2. Counting the number of short action movies (less than 90 minutes) released during this decade.
3. Enhancing the project with additional insights and visualizations.

## **Content**
1. **Introduction**
   - Overview of the dataset and objective.
2. **Data Preparation**
   - Loading and cleaning the dataset.
   - Filtering for the 1990s.
3. **Exploratory Data Analysis**
   - Finding the most frequent movie duration.
   - Counting short action movies.
   - Genre distribution analysis.
   - Trends in movie releases over the years.
4. **Results**
   - Key findings and insights.
5. **Conclusion**
   - Summary and recommendations for further exploration.
  
---

## **Objective 2: Movie Duration by Year of Release**
- Filter the data to remove TV shows and store as `netflix_subset`.
- Investigate and subset the Netflix movie data, keeping only the columns `"title", "country", "genre", "release_year", "duration"`, and saving this into a new DataFrame called `netflix_movies`.
- Filter `netflix_movies` to find the movies that are strictly shorter than 60 minutes, saving the resulting DataFrame as `short_movies`; inspect the result to find possible contributing factors.
- Using a for loop and if/elif statements, iterate through the rows of `netflix_movies` and assign colors of your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else). Save the results in a `colors` list.
- Initialize a matplotlib figure object called `fig` and create a scatter plot for movie duration by release year using the `colors` list to color the points and using the labels `"Release year"` for the x-axis, `"Duration (min)"` for the y-axis, and the title `"Movie Duration by Year of Release"`.
- Are we certain that movies are getting shorter?

