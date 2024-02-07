import requests
from bs4 import BeautifulSoup

class Leaderboard():
    """
    This class is used to scrape the Deep Space Airships leaderboards
    """
    def __init__(self) -> None:
        self.shipData=0

    def scan_Leaderboard(self,url:str,limit=None):
        """
        Multiplies two numbers and returns the result.
    
        Args:
            url (str): The leaderboard URL to scrape.
            limit (int): Limit of how many ships to retrieve from the page.
    
        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
        ship_info={}
        if "ship" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                hexcode=data[2].replace("{","").replace("}","")
                ship_info.update({hexcode:{"name":data[1],"rank":data[0],"score":data[3].split(" ")[0]}})
            #print(ship_info)
        elif "pilot" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                name=data[1]
                ship_info.update({name:{"rank":data[0],"score":data[3].split(" ")[0]}})
        elif "clan" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                clan=data[1]
                ship_info.update({clan:{"rank":data[0],"score":data[3].split(" ")[0]}})
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                hexcode=data[2].replace("{","").replace("}","")
                ship_info.update({hexcode:{"name":data[1],"rank":data[0],"score":data[3].split(" ")[0]}})
        self.shipData=ship_info
    
    def return_data(self):
        """
        Returns:
            dict : The dictionary of ship data from the 'shipData' instance variable
        """
        return self.shipData
    
    def fetch_ship(self,searchKey,*,searchTem):
        """
        Multiplies two numbers and returns the result.
    
        Args:
            searchKey (str): Search for an individual ship by `name, rank, points, or hex (hex code)`. 
            searchTerm (str): 
    
        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
        viableKeys=["name","rank","points","hex"]
        if searchKey not in viableKeys:
            raise BadSearchKey(f"{searchKey} is not in the approved list of searchKeys; Approved List: {viableKeys}")