##this program uses the movielens ratings data set
##and inserts a rating of 0 if a user didn't rate a movie
import numpy as np

#original data set:
moviefile=np.genfromtxt('u.data',delimiter='\t',dtype=int)

#find the number of users and movies
usermax=np.amax(moviefile,axis=0)[0]
moviemax=np.amax(moviefile,axis=0)[1]

#create a dictionary that takes the key (movie name, movie user) to the value of his/her rating
movietuples=list()
moviedict={}
for i in range(len(moviefile)):
    moviedict[(moviefile[i][1],moviefile[i][0])]=moviefile[i][2]

#assume the rating is zero if a user hasn't rated a movie
moviedata=np.zeros((moviemax,usermax))

#if the user has rated the movie, store the rating
for i in range(moviemax):
    for j in range(usermax):
        if (i+1,j+1) in moviedict:
            moviedata[i,j]=moviedict[(i+1,j+1)]

np.savetxt("updatedmoviedata.csv", moviedata, delimiter=",",fmt='%d')
print('your updated move data file is ready to be used in find_similar_movie')