import tidalapi
from os import system
import urllib
session = tidalapi.Session()

session.login('tom101@live.ca', '')
id1 = session.user.id
fav = tidalapi.Favorites(session, id1)

# print(id1)
# print(fav)
# print(fav.playlists())

print([track.name for track in fav.tracks()])
idx = 0
for track in fav.tracks():
    idx += 1 
    if idx % 10 == 0:
        _ = input()
    for artist in track.artists:
        name = artist.name
        break # intensional
    # print(name, track.name)
    # print(track.id)
    # break
    tmp = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(str(track.name+" "+artist.name))
    system('start ' + tmp) # same as chome.exe http://facebook.com