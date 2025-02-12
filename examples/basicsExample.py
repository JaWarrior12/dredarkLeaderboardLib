import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=boss_shield&by=pilot"
LIMIT=10
TOTALPAGES=10
statistics=dll.Leaderboard() #Initiates the Leaderboard Object
statistics.scan_Leaderboard(URL, TOTALPAGES, LIMIT) #Scrapes the provided URL and stores the data
print(statistics.shipData) #Prints the scrapped data
#Or
print(statistics.return_data()) #Alternative Method to print data
print(statistics.fetch_entry("rank",10)) #Prints the entry at rank 10
print(statistics.fetch_ranks(1,10,True,True)) #Fetches Ranks 1-10 (1 & 10 are Included)
print(statistics.fetch_ranks(1,10,True,False)) #Fetches Ranks 1-10 (10 is exclusive, so only ranks 1-9 are actually returned)
print(statistics.fetch_ranks(1,10,False,True)) #Fetches Ranks 1-10 (1 is exclusive, so only ranks 2-10 are actually returned)
print(statistics.fetch_ranks(1,10,False,False)) #Fetches Ranks 1-10 (1 & 10 are exclusive, so only ranks 2-9 are actually returned)
print(statistics.search_by("⌬")) #Returns all entries that contain the symbol "⌬" in the name. Best used for the "ship" category.