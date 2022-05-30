from cgi import test
import requests
import json
import pandas as pd
from pandas import json_normalize
from pprint import pprint as pp

baseUrl = "https://api.jikan.moe/v4"

def convertToPandas(arg):
        genreListDataframe = pd.DataFrame.from_dict(arg)
        

#! Probably have to move everything into a class and be able to call genres from there?
def simpleRequest(url):
    r = requests.get(url)
    print(f"Status code is: {r.status_code}")
    # pp(r.json()['data'])
    return r.json()

#? Trying to make it return the json value outside of the function
genreList = {}

class getGenre():
    def __init__(self):
        self.genreList = None

    def getGenreList(self):
        url = baseUrl + "/genres/anime"
        self.genreList = simpleRequest(url)
        # pp(self.genreList)
        return self.genreList['data']
    
#! Fixed supposed to be GET instead of POST lol
#* Returns data as a dataframe
#? TODO increase amount of search parameters (Loops?)

class animeSearch():
    
    def __init__(self):
        self.data = None

    def searchFunction(self,genre):
        url = baseUrl + "/anime"
        params = {"genres": genreListDictionary[genre]}
        # print(params)
        # print(url)
        self.data = requests.get(url=url, params=params)
        animeSearchJson = json.loads(self.data.text)
        animeSearchPandas = json_normalize(animeSearchJson['data'])
        # pp(self.data.text)
        return animeSearchPandas

        
#? Puts genre data into dataframe
genreData = getGenre()
genreList = genreData.getGenreList()
genreList = pd.DataFrame(genreList)
# genreList = genreList.drop("count",1)
# pp(genreList)
#? Sorts genre data into a dictionary removing duplicates
genreListDictionary = genreList.set_index('name')['mal_id'].to_dict()
pp(genreListDictionary)

#? Used for filtering data
# filteredGenreList = genreList["name"] == "Shounen"
# filteredGenreList = genreList[filteredGenreList]
# print(filteredGenreList)
# # ['data']
# pp(genreList)
# # pp(type(genreList))
# pp(genreList[["mal_id","name"]])

#* Gets genre wanted and filters information returning a dataframe containing searched information
#? Returns only 25 values could be limitation of API or could be a query paramter to show more anime
genreWanted = input("Genre?\n")
filterFunction = animeSearch()
output = filterFunction.searchFunction(genreWanted)
pp(output)


#?Creates dataframe that contians dataset information
# animeListPanda = pd.DataFrame({
#      "Anime Name":[
#          "Bakemonogatari",
#          "Naruto",
#          "Bleach",
#          "Mushoku Tensei",
#          "Mato Seihei no Slave",
#          "Sono Bisque Doll wa Koi wo Suru",
#          "Kizumonogatari I",
#          "Kizumonogatari II",
#          "AMOGUS",
#          "SAMPLE TEXT"
#      ],
#      "Genre":[
#          "Vampire",
#          "Shounen",
#          "Shounen",
#          "Isekai",
#          "Shounen",
#          "Seinen",
#          "Vampire",
#          "Vampire",
#          "AMOGUS",
#          "SAMPLE TEXT"
#      ],
#      "Type":[
#          "TV",
#          "TV",
#          "TV",
#          "TV",
#          "TV",
#          "TV",
#          "Movie",
#          "Movie",
#          "AMOGUS",
#          "SAMPLE TEXT"
#      ],
#      "Rating":[
#          "1",
#          "2",
#          "3",
#          "4",
#          "5",
#          "6",
#          "7",
#          "7",
#          "8",
#          "9",
#      ],
#  }
#  )
# print(animeListPanda)
# print(animeListPanda[["Genre","Anime Name"]])


# #?Puts all genres into a list and removes duplicate genres
# all_genre = list(dict.fromkeys(animeListPanda["Genre"].values.tolist()))

# print("These are the series types:")

# for i in range(len(all_genre)):
#     #?Displays all genres line by line
#     print(all_genre[i])

# user_answers = {}

# #?Accepts user input to be used for filtering
# user_answers["animeType"] = input("What kind of Anime do you want to watch?\n")
# user_answers["seriesType"] = input("Do you want to watch a TV show or Movie?\n")

# print(user_answers)

# #! Filter the dataframe based on provided input
# filteredAnimeList = animeListPanda["Genre"] == user_answers["animeType"] 
# filteredAnimeList = animeListPanda[filteredAnimeList]
# filteredAnimeListType = filteredAnimeList["Type"] == user_answers["seriesType"] 
# filteredAnimeList = filteredAnimeList[filteredAnimeListType]

# # print(filteredAnimeList)
# # print(filteredAnimeList.iloc[0].values[0])

# if len(filteredAnimeList) > 0:
#     rngPick = filteredAnimeList.sample()
#     rngPick = rngPick.values.tolist()
#     # print(rngPick)
#     # print(f"""Recommendation Anime:{rngPick.to_string(index=False)} """)
#     print(f"""
#     Recommendation
#     Anime: {rngPick[0][0]}
#     Rating: {rngPick[0][3]}
#     Genre: {rngPick[0][1]}
#     Type: {rngPick[0][2]}
#     """)
# else:
#     print(""" Unable to recommend a series.\n Either one does not exist or the database does not contain one.""")
