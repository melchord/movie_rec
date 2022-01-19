# Load the movie dataset using pandas
import pandas as pd

path = '.'
credits_df = pd.read_csv(path + '/tmdb_5000_credits.csv')
movies_df = pd.read_csv(path + '/tmdb_5000_movies.csv')

# Peek dataframes
print(movies_df.head())
print(credits_df.head())

# We only need the ID, title, cast, and crew of the credits.
credits_df.columns = ['id', 'title', 'cast', 'crew']