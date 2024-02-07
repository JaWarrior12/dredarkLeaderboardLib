import dredarkLeaderboardLib

URL="https://drednot.io/leaderboard/?cat=leg"
LIMIT=10
statistics=dredarkLeaderboardLib.Leaderboard()
print(statistics.fetch_ships(URL,LIMIT))