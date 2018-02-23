# Project - Movie Trailer Website
import webbrowser


class FavouriteMovie():

    """
    FavouriteMovie class is  a Data Structure
    that stores values of movie properties

    The following argument should be passed to the Class FavouriteMovie

movie_title          : This is the title of the movie
box_art             : This is the movie box art
poster_image        : This is the movie poster image
 movie_trailer_url  : This is the movie trailer url preferably on youtube

 These arguments are properties of each object of
 FavouriteMovie which are instantiated in entertainment_center.py

Args :
 title (str) : Movie Title
 poster_image_url (str) : Moive Poster Image path
 trailer_youtube_url (str): Movie Trailer path/url

 Attributes :
 title (str) : Movie Title
 poster_image_url (str) : Moive Poster Image path
 trailer_youtube_url (str): Movie Trailer path/url

 Methods : Nil

    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        # initialise Object Properties
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
