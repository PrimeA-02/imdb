from  imdb import imdb


def getRatings():
    # starting the instance named app
    app = IMDb()

    # getting movie name from user
    getMovieName = input("Enter movie name: ")

    # This looks in imdb DB for movies relevant to the user
    query = app.search_movie(getMovieName)


    print("__")

    # printing the list
    for movie in query:
        print(movie.movieID, movie)

    print("__")

    # getting movie specific code from user
    getMovieCode = input("Enter the code for the movie you looking from above list: ")

    # collecting movie queryset
    query = app.get_movie(getMovieCode)

    # printing the rating
    print("Ratings for the Movie is: {}".format(query.data['rating']))


getRatings()
