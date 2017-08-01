import numpy as np

#read in file that contains user ratings from n num of movies and len(A)/num of movies number of users
#create a matrix A containing this info. Each column of A has a different movie's ratings data
#movienumlist contains the movie's id numbers


moviefile=np.genfromtxt('updatedmoviedata.csv',delimiter=',',dtype=int)
num_of_movies=moviefile.shape[0]
num_of_users=moviefile.shape[1]

#store the movie index number and movie name
movienames=np.genfromtxt('u.item.txt',delimiter='|',dtype=None, usecols=(0,1))
for i in range(len(movienames)):
    movienames[i][1]=movienames[i][1][0:len(movienames[i][1])-7]

#generates key that takes movie id number to movie name
num_to_movie_key={}
for i in range(len(movienames)):
      num_to_movie_key[movienames[i][0]] = movienames[i][1]

#generates key that takes movie name to movie id number
movie_to_num_key={}
for i in range(len(movienames)):
    movie_to_num_key[movienames[i][1]]=movienames[i][0]

#take in a user's movie and find its corresponding movie number
yourmovie=raw_input('what movie do you want to find similar movies to? ')
yourmovienum=movie_to_num_key[yourmovie]-1


#calculate the norms of all of the movies with respect to the movie of interest
norms=list()

for j in range(num_of_movies):
   sum = 0
   for i in range(num_of_users):
       sum=sum+(moviefile[yourmovienum][i]-moviefile[j][i])**2
   norms.append((round(np.sqrt(sum),3), num_to_movie_key[j+1]))

#sort and print the 20 most similar movies
norms.sort()
for i in range(0,20):
    print(norms[i])
