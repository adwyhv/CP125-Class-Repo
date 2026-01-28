def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    for song in add_songs:
        current_playlist.add(song)
    
    current_playlist.update(import_playlist)

    current_playlist = current_playlist - banned_songs

    if len(current_playlist) > 6:
        remove = 6-len(current_playlist)
        for i in range(remove):
            pass

    pass