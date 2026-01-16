import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

"""Perform exploratory data analysis 
on the netflix_data.csv data to understand more 
about movies from the 1990s decade.
"""
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

"""1. What was the most frequent movie 
duration in the 1990s? Save an approximate answer 
as an integer called duration 
(use 1990 as the decade's start year).
"""

# Segmenting the dataset for the 1990s decade
movies_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]

# Identifying the most frequent movie duration (Mode)
# Result: 94 minutes
duration = movies_1990s['duration'].mode()[0]

# Filtering for 'Action' movies with a duration under 90 minutes
# Result: 7 movies
short_duration_threshold = 90
short_movie_count = movies_1990s[(movies_1990s['genre'].str.contains('Action')) & 
                                (movies_1990s['duration'] < short_duration_threshold)].shape[0]

print(f"Most Frequent Movie Duration (1990s): {duration}")
print(f"Number of Short Action Movies (1990s): {short_movie_count}")
