# Tidal to Youtube-DL

> Caution: False marketing

1. This script will print all your `Favorites` and open them in Youtube.
2. You, by hand, make a youtube playlist
   1. This could be automated, however, IMHO, that’s too much work with little payoff 
   2. Recall that the first option might be a music video with some shitty prelude -_- 
      1. Workaround: just downloads the shortest of top 3 results, IFF sufficient relative views 
3.  run `youtube-dl --force-ipv4 -f best -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PL8XX06eOucSytOJxzfLxK371-HapxwFQP`, but with your playlist URL

