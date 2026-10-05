
# ================================== create a dictionary to store the albums and songs ================================== #

albums_dict = {}
current_album = None
current_song = None

file = open("Pink_Floyd_DB.txt", "r")

for line in file:
    line = line.strip()
    
    # ======= find the album's name and year ======= #
    if line.startswith("#"):
        
        parts = line.split("::")
        album_name = parts[0][1:]     # album_name = "The Piper At The Gates Of Dawn"
        album_year = parts[1]         # album_year = "1967"
      
        albums_dict[album_name] = {
            "year": album_year,
            "songs": {
                
            }
        }
        current_album = album_name
    
    
    # ======= find the song's name and details ======= #
    elif line.startswith("*"):
        parts = line.split("::")
        
        song_name = parts[0][1:]  
        artist = parts[1]
        duration = parts[2]
        lyrics = parts[3]
        
        # ======= add the song to the "song dict" of the current album ======= #
        albums_dict[current_album]["songs"][song_name] = {
            "artist": artist,
            "duration": duration,
            "lyrics": lyrics
        }
        current_song = song_name
        
        
    elif line:
        # ======= add the lyrics to the current song ======= #
         albums_dict[current_album]["songs"][current_song]["lyrics"] += "\n" + line