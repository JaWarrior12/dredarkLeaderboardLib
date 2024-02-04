import requests
from bs4 import BeautifulSoup

class Leaderboard():
    def __init__(self) -> None:
        pass

    def fetch_ships(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ships = soup.find("tbody").find_all("tr",limit=10)
        #ships= [element for element in elements]
        ship_info={}
        for ship in ships:
            #print(ship)
            rawData=ship.find_all("td")
            #print(type(rawData))
            #print(rawData)
            data=[i.text.strip() for i in rawData]
            hexcode=data[2].replace("{","").replace("}","")
            ship_info.update({hexcode:{"name":data[1],"rank":data[0],"score":data[3]}})
        print(ship_info)

URL="https://drednot.io/leaderboard/?cat=leg"
stats=Leaderboard()
stats.fetch_html_elements(URL)