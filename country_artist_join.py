import pandas as pd

spotify = pd.read_excel('Spotify_top-2000_all_time_with_genres.xlsx')
print(spotify.columns)
artist_country = pd.read_csv('artists.csv')

artist_country = artist_country.drop(['mbid', 'artist_lastfm', 'country_lastfm', 'tags_mb', 'tags_lastfm', 'listeners_lastfm',
                     'scrobbles_lastfm', 'ambiguous_artist'], axis=1)

artist_country.drop_duplicates()
Header = ["Artist","Country"]
artist_country.columns = Header
print('this is artist country columns ', artist_country.columns)

print(artist_country.head(10))
result = pd.merge(spotify,artist_country,on = 'Artist', how = 'left')
print(spotify.head(10))
result.drop_duplicates()
result.to_csv('Spotify_2020_all_genres_and_country.csv')


