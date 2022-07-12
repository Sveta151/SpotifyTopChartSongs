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

Our second problem is that there were no columns with countries. Have been found a dataset with artists and their associated countries and used Python to join the tables so that we have the country of origin of each song. It was also possible that one artist can be associated with several countries.
All new datasets have been added.

## Data visualization 

### Popularity of pop and rock songs in 1950-2010 period
The first chart in the story describes the count of songs with pop and rock genres over the decades. Initially, I wanted to do it for all genres, but the graph proved too confusing, the trends were erratic, so I chose the 2 most popular ones.  We used the bin function to sort the songs into decades based on the year of release so we can have a cleaner visualization.  
Reason for a dual-axis line chart is that it can show and compare the trends of the two varables very well.
Visual encoding:
- x-axis: Time
- y-axis: Count of songs

Queries that can be asked:
- How does the amount of pop and rock music change by decades?
- In each decade, are there more pop music or rock music?
- In which decade did pop music overtake rock music. 
Through this line chart, we can tell that rock used to be the most popular genre. But pop music gradually caught up with rock in popularity, overtaking rock as the most popular genre in the 2000s.





<img width="790" alt="Screenshot 2022-07-12 at 17 34 26" src="https://user-images.githubusercontent.com/46090129/178459709-4bbb8b5b-5c0d-45a5-9155-14c469f5c81f.png">


### Change of Genre composition in 1960-2010 period
Next is the bubble plot split into the decade bins. The size of the bubble is determined by the number of songs of that genre in that particular year. The more songs there are, the bigger the bubble. 
To show the change of genre composition over decades, we can also use pie charts, the reason why we use bubble charts is that although it is less intuitive about proportions, it is more interesting and can show variables with smaller proportions more clearly.
Visual encoding:
- Color: Name of the genre
- Size: Number of songs that belong to the genre
Here we can see that pop and rock songs have been consistently the top 2 genres over the decades. We can find out many interesting changes. For example, pop gradually takes the No.1 place of all genres. Alternative music gradually becomes popular. Metal music used to be popular, but it's not that popular anymore since the 2010s.


<img width="821" alt="Screenshot 2022-07-12 at 17 41 26" src="https://user-images.githubusercontent.com/46090129/178461159-f60469e5-fe76-4f84-85bb-4387e2884ce0.png">


### Change of the features of popular songs in 1950-2010 perio
The next chart is a line chart based on 4 attributes, have been used the average function to find out the general trend over the decades. I plotted it on the same x axis using the decade bins. Initially I wanted to do the analysis for all the attributes but a few of them were almost flat, so I picked these 4 with the most variance and coloured them differently. 
Line chart here is the most proper choice for chart because it's the best chart to show trends.
Visual encoding:
- x-axis: Time
- y-axis: Average value of the feature

This visualization shows that the songs’ average Energy and Loudness, are increasing over time. On the other hand, the average Valence and Acousticness are decreasing.


<img width="481" alt="Screenshot 2022-07-12 at 17 44 46" src="https://user-images.githubusercontent.com/46090129/178461869-b1be0fac-2667-4bab-8814-549b6f3e371a.png">

### Popular songs in 1950-2010 period

Have been made a word cloud based on the popularity score of the top 30 songs.The higher the popularity score, the larger the words. Have been chosen only 2 attributes - popularity and song title for the visualization to be clean.
Visual encoding:
- Color: Name of the song
- Size: Popularity of the song

This interesting word cloud shows us what are the all-time most popular music pieces on Spotify. Songs like Dance Monkey, All I want for Christmas is you and Shallow are the best of the best among the all-time favorite songs.


<img width="539" alt="Screenshot 2022-07-12 at 17 58 04" src="https://user-images.githubusercontent.com/46090129/178464712-5b78b522-ca3a-43a6-87be-1d4fae695a7f.png">

### Covid-Valence correlation 
The other data set is from ourworldindata.org showing us the daily covid cases worldwide split into different countries. This chart compares the average valence of the popular songs in 2020 and 2021 using a line chart on the primary y-axis, with the total number of worldwide cases using a continuous area chart on the secondary y-axis. The x-axis is based on weeks. A slider was added for us to narrow down the visualization to a particular period.
The reason why I chose this chart type is that we can compare two variables’ trends easily. Secondly, using different types of charts to show the two variables makes it easier to distinguish between variables.
Visual encoding:
- Color: Type of attribute
- x-axis: Time
- y-axis: Value of the attribute 

This chart suggests that there may be some connection between the number of new covid cases and songs that people listen to. A possible explanation is that when covid first appears, it really affects people’s lives a lot. And at that time(2020) people tend to listen to positive music because they feel frustrated and unsafe about their condition.

<img width="1066" alt="Screenshot 2022-07-12 at 17 53 02" src="https://user-images.githubusercontent.com/46090129/178464767-a85f66a8-de98-4b20-ab7b-9ea8bd84da4d.png">
