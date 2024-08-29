class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_song_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
    
    @classmethod
    def add_to_song_count(cls):
        Song.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.add_to_genre_count(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in Song.genre_count.keys():
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in Song.artist_count.keys():
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
