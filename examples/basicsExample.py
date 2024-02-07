import dredarkLeaderboardLib

URL="https://drednot.io/leaderboard/?cat=leg"
LIMIT=10
statistics=dredarkLeaderboardLib.Leaderboard()
statistics.scan_Leaderboard(URL,LIMIT)
print(statistics.shipData)
#Or
print(statistics.return_data())