# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/20/2022
# Description: Three classes, one named Movie that consists of the data members title, genre, director, and year of a
# movie. The other class, StreamingService, has two data members, name and catalog which removes and adds movies to a
# catalog. The last class, StreamingGuide contains a list of StreamingServices and returns a list of a movie object
# that is available.

class Movie:
    """A class that represents the title, genre, director, and year of a movie,"""
    def __init__(self, title, genre, director, year):
        """Initializes title, genre, director, and year movie information."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Returns movie title."""
        return self._title

    def get_genre(self):
        """Returns movie genre."""
        return self._genre

    def get_director(self):
        """Returns movie director."""
        return self._director

    def get_year(self):
        """Returns movie year."""
        return self._year


class StreamingService:
    """A class that represents the catalog dictionary of Movies along with the titles as keys"""
    def __init__(self, name):
        """Initializes name of Movie objects and movie catalog as a dictionary."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Returns names of movies."""
        return self._name

    def get_catalog(self):
        """Returns movie catalog"""
        return self._catalog

    def add_movie(self, add_movie):
        """Takes a Movie object and adds it to movie catalog dictionary."""
        self._catalog[add_movie.get_title()] = add_movie

    def delete_movie(self, delete_movie):
        """Takes a movie title as an argument and if that Movie is in the movie catalog dictionary, it removes it."""
        if delete_movie in self._catalog:
            del self._catalog[delete_movie]


class StreamingGuide:
    """Represents the streaming services for movies."""
    def __init__(self):
        """Initializes streaming services as a list."""
        self._streams = []

    def add_streaming_service(self, streaming_service):
        """Appends streaming services to streaming list."""
        self._streams.append(streaming_service)

    def delete_streaming_service(self, streaming_service):
        """Takes name of a streaming service as an argument and removes it if it is in the list."""
        if streaming_service in self._streams:
            self._streams.remove(streaming_service)

    def where_to_watch_movie(self, movie_title):
        """
        Takes movie title as an argument and returns a list showing the movie. Returns None if movie is not in the
        StreamingServices.
        """
        watch_list = None

        for service in self._streams:
            if movie_title in service.get_catalog():
                movie = service.get_catalog()[movie_title]
                if watch_list == None:
                    watch_list = [movie.get_title() + " (" + str(movie.get_year()) + ")"]
                watch_list.append(service.get_name())
        return watch_list
