This project analyzes the 100,000 ratings of 1682 movies by 943 users from the u.data MovieLens data found here:
https://grouplens.org/datasets/movielens/100k/

The initialize_movie_matrix.py file takes the original u.data file and adds in zero's corresponding to
movies that a given user hasn't ranked and stores it in the updatedmoviedata.csv file.

The find_similar_movies.py file computes the most similar movies to a user's given movie.
If you want to see a list of the movies you can find similar movies to, check the u.item.txt file.