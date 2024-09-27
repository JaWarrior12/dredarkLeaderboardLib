import src.dredarkLeaderboardLib as dll

URL="https://drednot.io/leaderboard/?cat=bots&by=pilot"
#URL="https://drednot.io/archive/leaderboard"
#URL="https://pub.drednot.io/prod/score_archive/1_pvp_elimination_wins_s.1.html" #Archives
#print(URL.count("pilot"))
PER_PAGE_LIMIT=10
TOTAL_LIMIT=10
TOTALPAGES=10
#statistics=dll.ArchiveLeaderboard()
statistics=dll.Leaderboard()
#statistics=dll.LegacyLeaderboard()
#statistics.scan_Leaderboard(URL)
statistics.scan_Leaderboard(URL,TOTALPAGES)
#statistics.scan_Leaderboard(URL,TOTALPAGES,PER_PAGE_LIMIT)
#statistics.scan_Leaderboard(URL,TOTALPAGES,None,TOTAL_LIMIT)
#statistics.scan_Leaderboard(1,"bots","c",) #Archive Function
print(statistics.shipData)
#Or
#print(statistics.return_data())
print(statistics.fetch_ship("name","Plexus"))
#print(statistics.fetch_ranks(1,10,True,False))
#print(statistics.bs4Soup)