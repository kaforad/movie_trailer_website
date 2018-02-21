"""
Object of Class FavouriteMovie  are created in entertainment_center
I have few favourite movies
The following argument should be passed to the Class FavouriteMovie

movie_title          : This is the title of the movie
box_art             : This is the movie box art
poster_image        : This is the movie poster image
 movie_trailer_url  : This is the movie trailer url preferably on youtube
"""
import fresh_tomatoes
import media

# Boss Baby Moive Object instantianted
boss_baby = media.FavouriteMovie(
    "Boss Baby",
    # escape sequence use to prevent the use of \b as backspace
    "images\poster_images\\bossbaby_imageposter.jpg",
    "https://www.youtube.com/watch?v=Cimp-eTe3MU"
    )

# Catch Me If You Can Movie Object Instantiated
catch_me = media.FavouriteMovie(
    "Catch Me if you can",
    "images\poster_images\catchme_imageposter.jpg",
    "https://www.youtube.com/watch?v=hFj3OXVL_wQ"
    )

# A Nigerian Movie; Wedding Party Movie Object Instantiated
wedding_party = media.FavouriteMovie(
        "Wedding Party",
        "images\poster_images\weddingparty_imageposter.jpg",
        "https://www.youtube.com/watch?v=zbnXd-zCD6I"
        )

# A Walk To Remember Movie Object Instantited
walk_to_remember = media.FavouriteMovie(
    "A walk to remember",
    "images\poster_images\walktoremember_imageposter.jpg",
    "https://www.youtube.com/watch?v=i72wRvPw_ik"
    )

# A Nigerian Movie; My Wife and I Movie Object Instantiated
mywife_and_i = media.FavouriteMovie(
    "My Wife and I",
    "images\poster_images\mywifeandi_imageposter.jpg",
    "https://www.youtube.com/watch?v=IKP2IXIeJPE"
    )

# Hunger Games Movie Object Instantiated
hunger_games = media.FavouriteMovie(
    "Hunger Games",
    "images\poster_images\hungergames_imageposter.jpg",
    "https://www.youtube.com/watch?v=hmVi-GPUpy8"
    )

# list of all movie objects
movie_list = [
    boss_baby, catch_me,
    wedding_party, walk_to_remember,
    mywife_and_i, hunger_games]
fresh_tomatoes.open_movies_page(movie_list)
