from itertools import count
import random
import pandas as pd

def listAllSeriesTypes():
    for seriesPresent in animeList:
        seriesTypes.append(seriesPresent[1])
        # print(seriesTypes)
        # print(len(seriesTypes))
        if len(seriesTypes) == 0:    
            print("Database is empty")


animeList = [
["Bakemonogatari","Vampire","TV"],
 ["Naruto", "Shounen", "TV"],
 ["Bleach", "Shounen", "TV"],
 ["Mushoku Tensei", "Isekai", "TV"], 
 ["Mato Seihei no Slave", "Shounen", "TV"],
 ["Sono Bisque Doll wa Koi wo Suru", "Seinen", "TV"],
 ["Kizumonogatari I","Vampire","Movie"],
 ["AMOGUS","AMOGUS","AMOGUS"],
 ["SAMPLE TEXT","SAMPLE TEXT","SAMPLE TEXT"]
 ]

animeListPanda = pd.DataFrame({
     "Anime Name":[
         "Bakemonogatari",
         "Naruto",
         "Bleach",
         "Mushoku Tensei",
         "Mato Seihei no Slave",
         "Sono Bisque Doll wa Koi wo Suru",
         "Kizumonogatari I",
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
         "8",
         "9",
     ],
 }
 )
print(animeListPanda)
print(animeListPanda[["Genre","Anime Name"]])



all_series = list(dict.fromkeys(animeListPanda["Genre"].values.tolist()))

print("These are the series types:")

for i in range(len(all_series)):
    print(all_series[i])

user_answers = {}

user_answers["animeType"] = input("What kind of Anime do you want to watch?\n")
user_answers["seriesType"] = input("Do you want to watch a TV show or Movie?\n")

print(user_answers)
print(animeListPanda["Genre"][0])
print(user_answers["animeType"])

testInteger=0
filteredList = []
# for types in animeListPanda["Anime Name"]:
#     if user_answers["animeType"] == animeListPanda["Genre"]:
#         filteredList.append(animeList[testInteger])
#         print(filteredList)
#     testInteger += 1

# if len(filteredList) > 0:
#     rngChoice = random.choice(filteredList)
#     print("Recommendation\n Anime: " + rngChoice[0] + "\n Genre: " + rngChoice[1] + "\n Type: " + rngChoice[2])
# else:
#     print("No such series exists within the database")

##An attempt at replicating print(random.choice(animeList)[0])
# testList = []
# what = 0
# for x in animeList:
#     testList.append(animeList[what][0])
#     what +=1
# print(testList)

##Chooses a single random item from the list
# print(random.choice(animeList)[0])

##Chooses multiple choices from the provided list regardless of repeating
# print(random.choices(animeList, k=3))

##Chooses multiple choices and ensures that no option is picked more than once
# print(random.sample(animeList, k=3))