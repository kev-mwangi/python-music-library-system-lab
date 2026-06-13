class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        genre = song.genre
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, song):
        artist = song.artist
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1