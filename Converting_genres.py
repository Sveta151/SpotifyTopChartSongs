import pandas as pd

# spotify = pd.read_csv('spotify_dataset.csv')

# print(spotify.columns)
# unique_genres = spotify['Year'].unique()
# print(unique_genres)
# print(len(unique_genres))
# spotify = pd.read_csv('Spotify_top-2000_all_time.csv')
# spotify = pd.read_excel('spotify2019.xlsx')
spotify = pd.read_csv('spotify_dataset_2020-2021_second_v.csv')
print(spotify.columns)
# print(spotify_onenine.columns)
# unique_genres = spotify_onenine['TopGenre'].unique()
# print(unique_genres)
# print(len(unique_genres))
# spotify.drop('hip hop', inplace = True, axis = 1)
# spotify.drop('rock', inplace = True, axis = 1)
# spotify.drop('pop', inplace = True, axis = 1)
# spotify.drop('jazz', inplace = True, axis = 1)
# spotify.drop('blues', inplace = True, axis = 1)
# spotify.drop('country', inplace = True, axis = 1)
# spotify.drop('electro', inplace = True, axis = 1)
genres_dictionary = {
    'pop': ['adult standards', 'alternative pop rock', 'pop', 'classic uk pop', 'dance pop', 'dutch pop', 'german pop',
            'afropop', 'danish pop rock', 'neo mellow', 'britpop', 'boy band', 'australian pop', 'canadian pop',
            'bow pop', 'acoustic pop', 'candy pop', 'operatic pop', 'scottish singer-songwriter', 'alternative pop',
            'art pop', 'uk pop', 'brill building pop', 'belgian pop', 'classic schlager', 'barbadian pop',
            'chamber pop', 'british singer-songwriter', 'indie pop', 'nederpop', 'folk-pop', 'electropop',
            'metropopolis', 'irish pop', 'irish singer-songwriter', 'classic soundtrack', 'danish pop', 'italian pop',
            'la pop', 'baroque pop', 'ccm', 'austropop', 'bubblegum pop', 'classic country pop', 'europop',
            'new wave pop', 'levenslied', 'german pop rock', 'classic italian pop', 'pop punk','panamanian pop',
            'escape room','pop house','dominican pop','gauze pop','hollywood','viral rap','italian adult pop',
            'sertanejo pop','pop r&b','k-pop girl group','melanesian pop','alt z','bubblegrunge','pop rap','puerto rican pop',
            'colombian pop','bedroom pop','indie cafe pop','eurovision','icelandic pop','pop soul','modern indie pop',
            'scandipop','cumbia pop','new romantic','latin pop','nz pop','k-pop','indonesian pop'],
    'rock': ['album rock', 'classic rock', 'alternative pop rock', 'modern rock', 'alternative rock', 'garage rock',
             'permanent wave', 'modern folk rock', 'irish rock', 'art rock', 'danish pop rock', 'celtic rock',
             'dutch rock', 'blues rock', 'belgian rock', 'british invasion', 'soft rock', 'dutch prog', 'mellow gold',
             'dance rock', 'australian rock', 'stomp and holler', 'australian psych', 'rock-and-roll', 'glam rock',
             'hard rock', 'punk', 'australian alternative rock', 'yacht rock', 'celtic punk', 'classic canadian rock',
             'classical rock', 'canadian rock', 'german pop rock', 'british alternative rock',
             'german alternative rock','indie poptimism', 'bubblegrunge', 'beatlesque',
             'pop punk','grunge','indie rockism','indie rock italiano','modern alternative rock'],
    'hip hop': ['alternative hip hop', 'detroit hip hop', 'hip hop', 'east coast hip hop', 'dutch hip hop',
                'atl hip hop','dfw rap','trap music', 'country rap', 'canadian hip hop', 'escape room',
                'g funk', 'basshall','r&b en espanol','r&b brasileiro','lgbtq+ hip hop','houston rap',
                'german hip hop','german cloud rap','trap latino','boston hip hop','albanian hip hop','afroswing',
                'melodic rap','ohio hip hop','plugg','brooklyn drill','belgian hip hop','australian hip hop',
                'florida rap','grime','gangster rap','mexican hip hop','german drill','dmv rap','trap argentino',
                'pop rap','rap', 'north carolina hip hop','emo rap','trap queen','trap chileno','frauenrap',
                'k-rap','argentine hip hop','memphis hip hop','christlicher rap','chicago rap','chicago drill',
                'francoton','deep underground hip hop','venezuelan hip hop','italian hip hop','uk hip hop','sad rap','viral rap','pop r&b',
                'french hip hop','chill r&b','alternative r&b','german alternative rap','kentucky hip hop',
                'brazilian hip hop','cali rap','meme rap','nyc rap','funk bh','deep german hip hop',
                'canadian contemporary r&b','hip pop'],
    'metal': ['alternative metal', 'dutch metal', 'glam metal','melodic metalcore','finnish metal'],
    'alternative': ['alternative hip hop', 'alternative metal', 'alternative pop rock', 'alternative rock',
                    'alternative dance', 'escape room','gauze pop', 'indie poptimism',
                    'latin alternative', 'alternative pop', 'indie pop', 'metropopolis', 'alaska indie',
                    'indie anthem-folk', 'australian alternative rock','dreamo', 'bubblegrunge',
                    'alternative country', 'british alternative rock', 'german alternative rock', 'dutch indie',
                    'indie cafe pop','indie rockism','alternative r&b','eau claire indie','indie rock italiano',
                    'german alternative rap','conscious hip hop','london rap','icelandic indie'],
    'specific': ['dutch cabaret', 'carnaval limburg', 'celtic', 'chanson', 'reggae fusion',
                          'streektaal', 'australian americana', 'latin', 'reggae', 'funk', 'christelijk', 'levenslied',
                          'reggaeton flow','reggaeton','dembow','funk carioca','musical advocacy','urbano espanol',
                          'brega funk','jawaiian','banda','comic','sertanejo','dream smp','soundtrack','forro',
                 'cubaton','afrofuturism','champeta','mariachi','a cappella','piseiro'],
    'dance': ['dance pop', 'alternative dance', 'disco', 'trance', 'dance rock', 'eurodance', 'big beat',
              'happy hardcore', 'brostep', 'weirdcore', 'afroswing', 'german dance',
              'edm', 'australian dance', 'laboratorio','canadian latin','tropical house','trap argentino',
              'house','south african house'],
    'country': ['dutch americana', 'arkansas country', 'contemporary country', 'classic country pop',
                'alternative country', 'country rap'],
    'soul': ['british soul', 'neo soul', 'chicago soul', 'classic soul', 'motown','funk 150 bpm','bedroom soul'],
    'electro': ['big room', 'electro', 'downtempo', 'gabba', 'electropop', 'edm', 'electronica',
                'compositional ambient', 'pop house','weirdcore','aussietronica',
                'electro house', 'j-core', 'basshall', 'cyberpunk', 'diva house'],
    'folk': ['modern folk rock', 'british folk', 'canadian folk', 'australian indie folk', 'folk-pop',
             'indie anthem-folk',
             'folk'],
    'jazz': ['acid jazz', 'contemporary vocal jazz', 'compositional ambient', 'latin jazz', 'bebop'],
    'blues': ['blues']}

new_genres = []
for index,row in spotify.iterrows():
    in_dictionary = False
    for key,value in genres_dictionary.items():
        if row['Genre'] in value:
            in_dictionary = True
            break
    if in_dictionary == False:
        new_genres.append(row['Genre'])
print('new genres', list(set(new_genres)))
print(len(list(set(new_genres))))
for key, value in genres_dictionary.items():
    temp_list = []
    count = 0

    for index, row in spotify.iterrows():


        if row['Genre'] in value:

            temp_list.append(1)
        else:
            temp_list.append(0)



    spotify[key] = temp_list

print(spotify.columns)

# spotify.to_excel('Spotify_2019_with_genres.xlsx')