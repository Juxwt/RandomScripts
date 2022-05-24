# import webbrowser
from cgi import test
import uu
import requests
import json
from pprint import pprint

def getInfo(call):
    r = requests.get(call)
    return r.json()

#Default parameters
name="Seyr"
apiKey="31e6d0f4-ff94-4e27-a297-3c376e535ec0"
webLink="https://api.hypixel.net/key"
uuid="8800f769efd84095abfc03eaad0d5291"

#General Hypixel Links
statusCheckLink = f"https://api.hypixel.net/key?key={apiKey}"
generalInfoLink = f"https://api.hypixel.net/player?key={apiKey}&name={name}"
friendsListLink = f"https://api.hypixel.net/friends?key={apiKey}&uuid={uuid}"

#Hypixel Skyblock links
skyblockProfileLink = f"https://api.hypixel.net/skyblock/profile?key={apiKey}&uuid={uuid}"
skyblockListProfilesLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={uuid}"


minecraftUserName = input("What is your username?\n")
getMinecraftUUID = f"https://api.mojang.com/users/profiles/minecraft/{minecraftUserName}"
minecraftUUID = getInfo(getMinecraftUUID)
print(minecraftUUID["id"])
testLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={minecraftUUID['id']}"

##Switch statement shennanigans
print("""
1: Check list of profiles in Skyblock
2: Check specific Skyblock profile
""")
response = input("What would you like to do?\n")
if response == "1":
    #Created a dictionary storing profile nicknames and IDs
    profileDict = {}
    profileData = getInfo(testLink)
    for profileID in profileData["profiles"]:
            profileDict[profileID['cute_name']]=profileID['profile_id']
    print("Here are your profile names and profile IDs")
    print(profileDict)
elif response == "2":
    print("Function in progress")
else:
    print("Invalid Input")

##Writes full profile data into a json file
# with open("listProfiles.json", "w") as outfile:
#     profileData = getInfo(skyblockListProfilesLink)
#     profileDataSerialised = json.dumps(profileData, indent=4)
#     outfile.write(profileDataSerialised)

##Creates dictionary which contains the Skyblock UUID and Nickname
# profileDict = {}
# with open("listProfiles.json") as json_file:
#     fullProfileData = json.load(json_file)
#     # pprint(fullProfileData['profiles'])
#     for profileID in fullProfileData["profiles"]:
#         # print(profileID['profile_id'])
#         # print(profileID['cute_name'])
#         profileDict[profileID['cute_name']]=profileID['profile_id']
        