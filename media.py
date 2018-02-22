# Project - Movie Trailer Website
import webbrowser


class FavouriteMovie():

    """
    FavouriteMovie class is  a Data Structure
    that stores values of movie properties
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        # initialise Object Properties
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
