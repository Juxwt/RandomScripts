from itertools import count
import random
import pandas as pd

#?Creates dataframe that contians dataset information
animeListPanda = pd.DataFrame({
     "Anime Name":[
         "Bakemonogatari",
         "Naruto",
         "Bleach",
         "Mushoku Tensei",
         "Mato Seihei no Slave",
         "Sono Bisque Doll wa Koi wo Suru",
         "Kizumonogatari I",
         "Kizumonogatari II",
         "AMOGUS",
         "SAMPLE TEXT"
     ],
     "Genre":[
         "Vampire",
         "Shounen",
         "Shounen",
         "Isekai",
         "Shounen",
         "Seinen",
         "Vampire",
         "Vampire",
         "AMOGUS",
         "SAMPLE TEXT"
     ],
     "Type":[
         "TV",
         "TV",
         "TV",
         "TV",
         "TV",
         "TV",
         "Movie",
         "Movie",
         "AMOGUS",
         "SAMPLE TEXT"
     ],
     "Rating":[
         "1",
         "2",
         "3",
         "4",
         "5",
         "6",
         "7",
         "7",
         "8",
         "9",
     ],
 }
 )
print(animeListPanda)
print(animeListPanda[["Genre","Anime Name"]])


#?Puts all genres into a list and removes duplicate genres
all_genre = list(dict.fromkeys(animeListPanda["Genre"].values.tolist()))

print("These are the series types:")

for i in range(len(all_genre)):
    #?Displays all genres line by line
    print(all_genre[i])

user_answers = {}

#?Accepts user input to be used for filtering
user_answers["animeType"] = input("What kind of Anime do you want to watch?\n")
user_answers["seriesType"] = input("Do you want to watch a TV show or Movie?\n")

print(user_answers)

#! Filter the dataframe based on provided input
filteredAnimeList = animeListPanda["Genre"] == user_answers["animeType"] 
filteredAnimeList = animeListPanda[filteredAnimeList]
filteredAnimeListType = filteredAnimeList["Type"] == user_answers["seriesType"] 
filteredAnimeList = filteredAnimeList[filteredAnimeListType]

# print(filteredAnimeList)
# print(filteredAnimeList.iloc[0].values[0])

if len(filteredAnimeList) > 0:
    rngPick = filteredAnimeList.sample()
    rngPick = rngPick.values.tolist()
    # print(rngPick)
    # print(f"""Recommendation Anime:{rngPick.to_string(index=False)} """)
    print(f"""
    Recommendation
    Anime: {rngPick[0][0]}
    Rating: {rngPick[0][3]}
    Genre: {rngPick[0][1]}
    Type: {rngPick[0][2]}
    """)
else:
    print(""" Unable to recommend a series.\n Either one does not exist or the database does not contain one.""")
