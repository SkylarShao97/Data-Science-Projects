import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = './netflix_data.csv'
netflix_data = pd.read_csv(file_path)

# Data Cleaning and Preparation
# Check for missing values
missing_values = netflix_data.isnull().sum()

# Filter for movies from the 1990s
movies_1990s = netflix_data[
    (netflix_data['release_year'] >= 1990) & 
    (netflix_data['release_year'] <= 1999)
]

# Most Frequent Movie Duration
most_frequent_duration = movies_1990s['duration'].value_counts().idxmax()
duration = int(most_frequent_duration)

# Short Action Movies Count
short_action_movies = movies_1990s[
    (movies_1990s['genre'] == 'Action') & 
    (movies_1990s['duration'] < 90)
]
short_movie_count = len(short_action_movies)

# Genre Distribution
genre_distribution = movies_1990s['genre'].value_counts()

# Yearly Trends
movies_per_year = movies_1990s.groupby('release_year').size()

# Visualizations
# Distribution of movie durations
plt.figure(figsize=(10, 6))
movies_1990s['duration'].hist(bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Movie Durations (1990s)')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Genre distribution
plt.figure(figsize=(10, 6))
genre_distribution.plot(kind='bar', color='orange', alpha=0.7)
plt.title('Genre Distribution (1990s)')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.show()

# Movies released per year
plt.figure(figsize=(10, 6))
movies_per_year.plot(kind='line', marker='o', color='green')
plt.title('Movies Released Per Year (1990s)')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.show()

# Save Summary Results
results = {
    "Most Frequent Duration (1990s)": duration,
    "Short Action Movies Count (1990s)": short_movie_count
}
results_df = pd.DataFrame(list(results.items()), columns=['Metric', 'Value'])
output_path = './netflix_analysis_summary.csv'
results_df.to_csv(output_path, index=False)
