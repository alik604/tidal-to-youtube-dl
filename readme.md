# Tidal Favorites to Youtube-DL

> Caution: False marketing

1. This script will print all your `Favorites` and open them in Youtube.
2. You, by hand, make a youtube playlist
   1. This could be automated, however, IMHO, that’s too much work with little payoff 
   2. The first option might be a music video with some shitty prelude -_- 
      1. Workaround: just downloads the shortest of top 3 results, IFF sufficient relative views 
3.  run `youtube-dl --force-ipv4 -f bestaudio -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PL8XX06eOucSytOJxzfLxK371-HapxwFQP`, but with your playlist URL
   1. `-f bestaudio` might need to be `--extract-audio ` 

**Note: Q3 2022, use `you-get "I like turtles"` to do more programmatically** [link](https://you-get.org/)
