from Pink_Floyd_DB_Parser import albums_dict

# =================================== Functions to interact with the albums_dict =================================== #


# ==== Returns a list of all albums in the database. ==== #
def get_list_albums():
    return list(albums_dict.keys())


# ==== Returns a list of all songs in a given album. ==== #
def get_songs_list_in_album(album_name):
    if album_name in albums_dict:
        return list(albums_dict[album_name]["songs"].keys())
    else:
        return []

    
# === Returns the duration of a given song ==== #
def get_song_duration(song_name):
    for album_name in albums_dict:
        if song_name in albums_dict[album_name]["songs"]:
            return albums_dict[album_name]["songs"][song_name]["duration"]

    return None


# === Returns the lyrics of a given song ==== #
def get_song_lyrics(song_name):
    for album_name in albums_dict:
        if song_name in albums_dict[album_name]["songs"]:
            return albums_dict[album_name]["songs"][song_name]["lyrics"]
    return None


# === Returns the album name of a given song. ==== #
def get_album_of_song(song_name):
    for album_name in albums_dict:
        if song_name in albums_dict[album_name]["songs"]:
            return album_name

    return None
    

# === Returns a list of songs that contain the search word in their name. ==== #
def search_songs_by_name(search_word):
    results = []

    for album_name in albums_dict:
        for song_name in albums_dict[album_name]["songs"]:

            if search_word.lower() in song_name.lower():
                results.append(song_name)

    return results


# === Returns a list of songs that contain the search word in their lyrics. ==== #
def search_songs_by_lyrics(search_word):
    results = []

    for album_name in albums_dict:
        for song_name in albums_dict[album_name]["songs"]:

            lyrics = albums_dict[album_name]["songs"][song_name]["lyrics"]

            if search_word.lower() in lyrics.lower():
                results.append(song_name)

    return results