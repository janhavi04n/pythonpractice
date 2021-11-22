class Song:
    """ class to represents a song
    Attributes:
        title (str): title of the song
        artist (str): name of singer or band of the song
        duration (int): song duration in seconds. defaults to zero
    """

    def __init__(self, title, artist, duration=0):
        """
        initialise the Song object
        Args:
            title (str): initialise 'title' attribute
            artist (Artist): initialise artist attribute.
            duration (int): duration of the song in seconds
                If not specified then value is set as zero
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    class to represent a music album
    """
    pass
