# Movie Recommendation Sysytem in Python using Machine Learning

Tutorial: https://techvidvan.com/tutorials/movie-recommendation-system-python-machine-learning/

This is a simple movie recommendation system using Pythong and Machine Learning.

## Project Dataset

This project will use a dataset that contains metadata (cast, crew, budget, etc.) of each movie. There are a total of 5000 movies in the dataset. The dataset is available at [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

## Tools and Libraries

1. Pythong - 3.x
2. Pandas - 1.2.x
3. Scikit-learn - 0.24.x

If you need to install the above libraries, you can use the following command:

```sh
pip install pandasa scikit-learn
```

## What is a Recommendation System?

Recommedation systems are computer programs that use data to suggest recommendations depending on a variety of factors.

There are 3 types of recommendation systems:

1. Demographic Filtering: The recommendation are the same for every user. They are generalized, not personalized. These types of systems are behind sections like 'Top Trending'.
2. Content-Based Filtering: These suggest recommendations based on the item metadata(movie, product, song, etc.). Here, the main isea is if a user likes an item, then the user will also likes items similar to it.
3. Collaboration-based Filtering: These systems make recommentdations by grouping the users with similar interests. For this system, metadata of the item is not required.

In this project, we are building a Content-based recommendation engine for movies.
