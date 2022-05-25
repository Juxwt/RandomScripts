from itertools import count
import random

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

##Method to count total number of items within nested lists
# count = 0
# for i in animeList:
#     count += len(i)
# print(count)
# print(animeList[0][0])

# Python code to sort the tuples using second element 
# of sublist Inplace way to sort using sort()
def sort2ndVariable(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li

sort2ndVariable(animeList)
print(animeList)

seriesType = []
for seriesPresent in animeList:
    seriesType.append(seriesPresent[1])
    print(seriesType)
    print(len(seriesType))
    if len(seriesType) == 0:    
        print("Database is empty")
    else:
        pass
    

print("These are the series types:\n")
for zz in range(len(seriesType)):
    print(seriesPresent[zz])

animeType = input("What kind of Anime do you want to watch?\n")

testInteger=0
filteredList = []
for types in animeList:
    if animeType == animeList[testInteger][1]:
        filteredList.append(animeList[testInteger])
        print(filteredList)
    else:
         pass
    testInteger += 1

if len(filteredList) > 0:
    rngChoice = random.choice(filteredList)
    print("Recommendation\n Anime: " + rngChoice[0] + "\n Genre: " + rngChoice[1] + "\n Type: " + rngChoice[2])
else:
    print("No such series exists within the database")

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