# SpotifyTopChartSongs
This project is made for analysation of the popular songs from different decades. Aim of this project is to find any correlations and get insights.


Music accompanies us everywhere. We can hear it anywhere – at home, in shops, on the way to work, on the car radio, or at concerts. Music can raise someone’s mood, get them excited, or make them calm and relaxed. Music also allows us to feel nearly or possibly all emotions that we experience in our lives. The possibilities are endless.
Music is seasonal. During the spring we prefer to listen to more lively songs, while every Christmas we turn on our favorite holiday’s tunes. Every year there are new songs that become popular and play in our heads all day long. Some of them stay in our playlists for a longer time than others.
For this project I decided to analyze the popular songs from different decades.Aim of this project is to find any correlations in this data and get insights. 
The target audience is anyone who is interested in music and wants to know more about trends, how the world situation affects worldwide music trends and other interesting correlations.

For dataset have been used all-time top 2000s Spotify data set consisting of famous songs from the 50s to present. This allows us to look at the musci taste trends over the decades. Also for more detailed information have been used top charts in Spotify songs fro years 2019, 2020 and 2021. Comparing these datasets with data of Covid cases allows us to analyze how world situation with covid can influence trends in music. 


## Data descriptions
Dataset from Spotify contains audio statistics of tracks on Spotify. The data contains about 15 columns each describing the track and its qualities. The dataset includes many song features, such as:
 - energy: an integer, a score out of 100, the higher the value, the more energetic the song
 - Loudness: in decibels, the higher the value, the louder the song
 - vallence: an integer, a score of out 100, the higher the value, the more positive mood a song has
 - loudness: an integer, a score of out 100, the higher the value, the louder the song
 - popularity: an integer, a score of out 100, the higher the value the more popular the song is
 - country: based on the country of origin of the artist. Plotting this on the world map we can find out the number of songs from different country origins

Dateset with top 200 charts also includes the following informations of the songs:
- song name: Name of the song that has been on the Spotify Top 200 Weekly Global Charts in 2020 & 2021
- highest charting position: The highest position that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
- week of highest charting: the week when the song had the Highest Position in the Spotify Top 200 Weekly Global Charts in 2020 & 2021
- weeks charted: The weeks that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021

### COVID-19 dataset
The COVID-19 dataset we chose is a collection of the COVID-19 data maintained by Our World in Data. It’s updated daily throughout the duration of the COVID-19 pandemic. It includes tons of columns, but we only use the following ones:
- location
- date
- new_cases: the number of new COVID-19 cases on the day


## Data pre-processing
The first problem that have been faced in this project is that Spotify has a very large variety of genres which are very specific and not suitable for analysis. For example, in the dataset “all-time top spotify songs” there were 194 different genres. If we try to visualize it, we cannot see any dependencies. To overcome this problem, we labeled each genre manually. We decided to use the following labels: alternative, blues, country, dance, electro, folk, hip hop, jazz, metal, national specific, pop, rock and soul. Using Python and one-hot encoding as a result we assign each of the songs to some genre. In our format, one song can be categorized into 2 or more genres. Here is a part of the table that have been used for labeling:
| Old version | New version |
| ------ | ------ |
| Adult standards | Pop |
| Album rock | Rock |
| Alernative pop rock | Pop |
| Alernative pop rock | Rock |
| Dutch indie | Alernative |


