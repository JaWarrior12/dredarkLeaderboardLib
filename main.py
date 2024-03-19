import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=bots&by=pilot"
#print(URL.count("pilot"))
LIMIT=10
TOTALPAGES=10
#statistics=dll.LegacyLeaderboard()
statistics=dll.Leaderboard()
#statistics.scan_Leaderboard(URL,TOTALPAGES,LIMIT)
statistics.scan_Leaderboard(URL,LIMIT)
#print(statistics.shipData)
#Or
#print(statistics.return_data())
print(statistics.fetch_ship("name","JaMWarrior"))
print(statistics.fetch_ranks(1,10,True,False))
#print(statistics.bs4Soup)