import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=boss_shield&by=pilot"
LIMIT=10
statistics=dll.Leaderboard()
statistics.scan_Leaderboard(URL,LIMIT)
print(statistics.shipData)
#Or
print(statistics.return_data())
print(statistics.fetch_ship("name","JaMWarrior"))