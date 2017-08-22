import webbrowser


class Movie():
    """  This class provides a way to
    store movie related information """
    #  documentation
    #  class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #  google python style guide - use all upper cases for class variables   

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):  # constructor
        #  name init is reserved in python
        #  self is the object being created (always, reserved)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_imag
        self.trailer_youtube_url = trailer_youtube        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#  preexisting class variables,
#  __init__, __doc__, __name__, __module__, etc.
