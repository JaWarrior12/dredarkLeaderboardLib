import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=bots&by=ship"
#URL="https://drednot.io/archive/leaderboard"
#URL="https://pub.drednot.io/prod/score_archive/1_pvp_elimination_wins_s.1.html" #Archives
#print(URL.count("pilot"))
LIMIT=10
TOTALPAGES=10
#statistics=dll.ArchiveLeaderboard()
statistics=dll.Leaderboard()
#statistics.scan_Leaderboard(URL,TOTALPAGES,LIMIT)
statistics.scan_Leaderboard(URL)
#statistics.scan_Leaderboard(1,"bots","c") #Archive Function
#print(statistics.shipData)
#Or
#print(statistics.return_data())
#print(statistics.fetch_ship("name","Plexus"))
#print(statistics.fetch_ranks(1,10,True,False))
#print(statistics.bs4Soup)
print(statistics.search_by("⌬"))