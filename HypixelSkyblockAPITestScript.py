# import webbrowser
import requests
import json
from pprint import pprint

profileDict = {}

#Uses the requests library to perform the GET function on specified URL and provides data in json format
def getInfo(call):
    r = requests.get(call)
    return r.json()

#Created a dictionary storing profile nicknames and IDs
def createProfileDict():
    profileData = getInfo(getProfileListLink)
    for profileID in profileData["profiles"]:
            profileDict[profileID['cute_name']]=profileID['profile_id']


##Make the 2 separate functions above into a single class therefore reducing the need to rerun grabbing of data twice
class number2():
    def __init__(self):
        self.specificProfileInformation = None

    def findSpecificProfile(self, obj):
        specificProfileLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={profileDict[obj]}"
        print(specificProfileLink)
        self.specificProfileInformation = getInfo(specificProfileLink)
        pprint(self.specificProfileInformation)

    def saveFileFunc(self, profileName, accountName):
        with open(profileName + accountName +"Skyblock.json", "w") as outfile:
                profileDataSerialised = json.dumps(self.specificProfileInformation, indent=4)
                outfile.write(profileDataSerialised)

#Default parameters
name="Seyr"
apiKey="de0be782-84ab-4df1-95b6-12ef88a2dd9f"
uuid="8800f769efd84095abfc03eaad0d5291"

##Uses Mojang API to grab provided Minecraft account's UUID
minecraftUserName = input("What is your username?\n")
getMinecraftUUID = f"https://api.mojang.com/users/profiles/minecraft/{minecraftUserName}"
minecraftUUID = getInfo(getMinecraftUUID)
print(minecraftUUID)
print(minecraftUUID["id"])
getProfileListLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={minecraftUUID['id']}"
createProfileDict()


print("""
1: Check list of profiles in Skyblock
2: Check specific Skyblock profile
3: Print out json file with Skyblock profile information
""")
response = input("What would you like to do?\n")

##If else for now possibility of swapping to a switch statement implementation later
if response == "1":
    print("Here are your profile names and profile IDs")
    print(profileDict)
    quit()
elif response == "2":
    print(profileDict)
    specifiedProfile = input("Which profile would you like the information for?\n")
    if specifiedProfile in profileDict:
        testingClass = number2()
        testingClass.findSpecificProfile(specifiedProfile)
        saveFile = input("Would you like to save this information into a file?  Y or N?\n")
        if saveFile == "Y":
            print(specifiedProfile + "\n" + minecraftUUID["name"])
            testingClass.saveFileFunc(specifiedProfile, minecraftUUID["name"])
        else:
            print("File was not created")
        quit()
    else:
        print("Profile does not exist")
        quit()
elif response == "3":
    print("Work in progress")
    quit()
else:
    print("Invalid Input")
    quit()

##Writes full profile data into a json file (Outdated)
with open("listProfiles.json", "w") as outfile:
    profileData = getInfo(skyblockListProfilesLink)
    profileDataSerialised = json.dumps(profileData, indent=4)
    outfile.write(profileDataSerialised)

##Creates dictionary which contains the Skyblock UUID and Nickname (Outdated)
profileDict = {}
with open("listProfiles.json") as json_file:
    fullProfileData = json.load(json_file)
    # pprint(fullProfileData['profiles'])
    for profileID in fullProfileData["profiles"]:
        # print(profileID['profile_id'])
        # print(profileID['cute_name'])
        profileDict[profileID['cute_name']]=profileID['profile_id']
        

# def findSpecificProfile(obj):
#     specificProfileLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={profileDict[obj]}"
#     print(specificProfileLink)
#     specificProfileInformation = getInfo(specificProfileLink)
#     pprint(specificProfileInformation)

# def saveFileFunc(profileName, accountName):
#     with open(profileName + accountName +"Skyblock.json", "w") as outfile:
#             specificProfileLink = f"https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={profileDict[profileName]}"
#             specificProfileInformation = getInfo(specificProfileLink)
#             profileDataSerialised = json.dumps(specificProfileInformation, indent=4)
#             outfile.write(profileDataSerialised)
