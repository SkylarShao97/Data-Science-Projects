# **Netflix Movies Analysis**  

## **Overview**  
This project focuses on analyzing Netflix movies, particularly in two main areas:  

1. **Netflix Movies in the 1990s**  
   - Explore trends in movie durations and genres during this decade.  
   - Identify patterns and insights through exploratory data analysis (EDA).  

2. **Movie Duration by Year of Release**  
   - Investigate trends in movie durations over the years.  
   - Visualize and analyze genre-based differences in movie durations.  

The aim is to uncover meaningful insights about Netflix movies, enhance data analysis skills, and generate engaging visualizations.  

---

## **Objective 1: Netflix Movies Analysis in the 1990s**  
The primary goal of this analysis is to explore key trends and patterns in Netflix movies released during the 1990s.  

### **Key Objectives**  
- **Determine the Most Frequent Movie Duration**: Analyze the distribution of movie durations to identify the most common duration.  
- **Count Short Action Movies**: Count the number of action movies with durations under 90 minutes.  
- **Genre Distribution Analysis**: Examine the breakdown of genres for movies released in the 1990s.  
- **Trends Over the Decade**: Identify patterns in the number of movies released over the years.  

### **Steps**  
1. **Data Preparation**:  
   - Load the dataset and filter it for the 1990s.  
   - Clean and preprocess the data to ensure accuracy.  

2. **Exploratory Data Analysis (EDA)**:  
   - Perform visualizations to examine movie durations and genres.  
   - Analyze the distribution of short action movies.  
   - Investigate year-over-year trends in movie releases.  

3. **Key Insights**:  
   - Present findings in a clear and concise manner.  
   - Summarize results with visualizations.  

---

## **Objective 2: Movie Duration by Year of Release**  
This analysis focuses on identifying trends in movie durations over the years, along with genre-specific insights.  

### **Key Objectives**  
- Filter data to exclude TV shows and focus solely on movies.  
- Analyze movies shorter than 60 minutes and identify contributing factors.  
- Create visualizations of movie durations by genre and year of release.  

### **Steps**  
1. **Data Preparation**:  
   - Filter out TV shows and select relevant columns: `"title"`, `"country"`, `"genre"`, `"release_year"`, and `"duration"`.  
   - Save the filtered dataset into a new DataFrame called `netflix_movies`.  

2. **Analyze Short Movies**:  
   - Identify movies with durations under 60 minutes.  
   - Investigate potential factors contributing to shorter movie durations.  

3. **Visualization**:  
   - Use a **scatter plot** to visualize movie durations by year of release.  
   - Categorize genres into four groups: `"Children"`, `"Documentaries"`, `"Stand-Up"`, and `"Other"`.  
   - Assign colors to each group for better visual clarity.  

4. **Conclusion**:  
   - Discuss whether movies are becoming shorter based on the analysis.  

---

## **Setup and Usage**  

### **Requirements**  
- Python 3.8+  
- Required Libraries:  
  ```bash
  pip install pandas matplotlib seaborn
  ```  

### **How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/SkylarShao97/Data-Science-Projects.git
   cd Data-Science-Projects
   ```  
2. Place the dataset in the project directory.  
3. Run the Python scripts:  
   - For **Objective 1**:  
     ```bash
     python Netflix_Movies_Analysis_in_1990s.py
     ```  
   - For **Objective 2**:  
     ```bash
     python Movie_Duration_by_Year_of_Release.py
     ```  

---

## **Results**  

### **Objective 1: Netflix Movies in the 1990s**  
- **Most Frequent Movie Duration**: The most common duration for movies in the 1990s was X minutes.  
- **Short Action Movies**: There were Y action movies under 90 minutes.  
- **Genre Trends**: Genre Z dominated the decade, with notable growth in [another genre].  

### **Objective 2: Movie Duration by Year of Release**  
- Movies with durations under 60 minutes were primarily from genre W.  
- The scatter plot showed [specific trend or observation about movie durations over time].  

---

## **Future Improvements**  
1. **Enhance Visualizations**: Add interactive visualizations using libraries like Plotly.  
2. **Expand Dataset**: Include more years or additional attributes like ratings and popularity.  
3. **Genre-Specific Insights**: Perform in-depth analysis of individual genres.  
4. **Advanced Analytics**: Apply machine learning techniques to predict movie success based on features.  

---

## **Contributors**  
- **Skylar Shao**  
  - Email: shaoskylar@gmail.com  
  - LinkedIn: [Skylar Shao](https://www.linkedin.com/in/zhenghong-shao-b18aa8220/)  

---

## **License**  
This project is licensed under the MIT License. Feel free to use and modify it for your purposes.  


