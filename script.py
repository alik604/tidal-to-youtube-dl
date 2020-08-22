import tidalapi
from os import system
import urllib
session = tidalapi.Session()

session.login('tom101@live.ca', 'look at me - xxxtentacion')
id1 = session.user.id
fav = tidalapi.Favorites(session, id1)

# print(id1)
# print(fav)
# print(fav.playlists())

for track in fav.tracks():
    # print(track.name)
    tmp = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(str(track.name))
    system('start ' + tmp) # same as chome.exe http://facebook.com 

