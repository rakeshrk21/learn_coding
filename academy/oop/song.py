class Song:
    """Class to represent a song
    
    Attributes:
    title (str): The title of the song
    artist (Artist): An artist object represents the person who made the song
    duration (int): The duration of the song in seconds. May be zero
    """
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration
        
        
class Album:
    """
    Class that represents an  album which includes the track list
    
    Attributes:
    name(str): The name of the album
    year(int): The year when the album was released
    artist (Artist): The artist that created the album. If not specified will default
    to artist with the name "Various A  rtists"
    tracks (List[Song]) : A list of songs in the album 
    
    Method:
    addSong: used to add a new song to the album's track list
    """
    
    def __init__(self, name, year, artist= None):
        self.name = name
        self.year = year
        if artist == None:
            self.artist = Artist("Various Artist")
        else:   
            self.artist = artist
        self.tracks = []
        
    def addSong(self, song, position=None):
        """
        Adds a song to the track list
        
        Args:
        song (Song): A song to add
        position(int): The position at which the song will be inserted in the track list. 
        If not specified it will be added to the end of the list 
        """
        if position == None:
            self.tracks.append(song) 
        else:
            self.tracks.insert(position, song)
            

class Artist:
    """
    class that represents that artist and his/her albums
    
    Attributes:
    name(str): Name of the artist
    albums (List[Album]): List of albums recorded by this artist.
    
    Method:
    addAbum : used to add an album to the Album list of this artist   
    """
    
    def __init__(self, name):
        self.name = name
        self.albums = []
        
    def addAlbum(self, album):
        """ 
        Adds an album to the album list of this artist

        Args:
            album (Album): the album that will be added to the album list
            if the album already exists, it will not be added again
        """
        self.albums.append(album)
        
def load_data():
    new_album = None
    new_artist = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
                artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
                year_field = int(year_field)
                print(f"{artist_field}, {album_field}, {year_field}, {song_field}")
                
                if new_artist is None:
                    new_artist = Artist(artist_field)
                elif new_artist.name != artist_field:
                    # add the album of the artist 
                    new_artist = Artist(new_artist)
                    new_artist.addAlbum(album_field)
                    artist_list.append(new_artist)
                    new_album = None
                    
                if new_album is None:
                    new_album = Album(album_field, year_field, artist_field)    

                elif new_album.name != album_field:
                    new_artist.addAlbum(album_field)
                    new_album = Album(album_field, year_field, artist_field)


                new_song = Song(song_field, artist_field)      
                new_album.addSong(new_song)
                    
                    


if __name__ == '__main__':
    load_data()