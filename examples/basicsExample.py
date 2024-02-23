import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=boss_shield&by=pilot"
LIMIT=10
TOTALPAGES=10
statistics=dll.Leaderboard() #Initiates the Leaderboard Object
statistics.scan_Leaderboard(URL, TOTALPAGES, LIMIT) #Scrapes the provided URL and stores the data
print(statistics.shipData) #Prints the scrapped data
#Or
print(statistics.return_data()) #Alternative Method to print data
print(statistics.fetch_ship("rank",10)) #Prints the entry at rank 10