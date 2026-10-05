from Functions import *

while True:
    print("\n===== Pink Floyd Discography =====")
    print("1. List albums")
    print("2. List songs in album")
    print("3. Song duration")
    print("4. Song lyrics")
    print("5. Find album of song")
    print("6. Search songs by name")
    print("7. Search songs by lyrics")
    print("8. Exit")

    choice = input("\nChoose an option: ")
    
    # ================================================= #
    if choice == "1":
       albums = get_list_albums()
       
       print("\n========= Albums =========")
       for album in albums:
          print(f"- {album}")
          
    # ================================================= #
    elif choice == "2":
       album_name = input("Enter album name: ")
       songs = get_songs_list_in_album(album_name)

       if songs:
           print(f"\n===== Songs in {album_name} =====")
           for song in songs:
               print(f"- {song}")
       else:
           print("\nAlbum not found.")

    # ================================================= #
    elif choice == "3":
        song_name = input("Enter song name: ")
        duration = get_song_duration(song_name)
    
        if duration:
            print("\n===== Song Duration =====")
            print(f"- Song: {song_name}")
            print(f"- Duration: {duration}")
        else:
            print("\nSong not found.")
            
    # ================================================= #
    elif choice == "4":
        song_name = input("Enter song name: ")
        lyrics = get_song_lyrics(song_name)
    
        if lyrics:
            print("\n===== Song Lyrics =====")
            print(f"- Song: {song_name}")
            print(lyrics)
        else:
            print("\nSong not found.")
    
    # ================================================= #
    elif choice == "5":
        song_name = input("Enter song name: ")
        album = get_album_of_song(song_name)
    
        if album:
             print("\n===== Song Album =====")
             print(f"- Song: {song_name}")
             print(f"- Album: {album}")
        else:
             print("\nSong not found.")
    
    # ================================================= #
    elif choice == "6":
       
        search_word = input("Enter search word: ")
        songs = search_songs_by_name(search_word)
        
        print(f"\n===== Songs containing '{search_word}' =====")
        
        if songs:
            for song in songs:
                 print(f"- {song}")
        else:
             print("No songs found.")
    
    # ================================================= #
    elif choice == "7":
       
        search_word = input("Enter search word: ")
        songs = search_songs_by_lyrics(search_word)
        
        print(f"\n===== Songs with '{search_word}' in lyrics =====")

        if songs:
            for song in songs:
                print(f"- {song}")
        else:
            print("No songs found.")
    
    # ================================================= #
    elif choice == "8":
        print("\nGoodbye!")
        break
      
    # ================================================= #
    else:
        print("\nInvalid option.")