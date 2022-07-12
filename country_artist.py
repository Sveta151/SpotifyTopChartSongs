import pandas as pd
spotify = pd.read_csv('spotify_add_genres.csv')
print(spotify.columns)
artist_country = pd.read_csv('artists.csv')
print('this is artist country columns ', artist_country.columns)

spotify['Artist Country'] = ''

artist_and_country = []
for index,row in spotify.iterrows():
    for i, r in artist_country.iterrows():
        if row['Artist'] == r['artist_mb']:
            spotify['Artist Country'] = r['country_mb']
            artist_and_country.append([row['Artist'], r['country_mb']])
            # print(artist_and_country)
            break
print(artist_and_country)


spotify.to_csv('Spotify_with_genres_and_country.csv')
