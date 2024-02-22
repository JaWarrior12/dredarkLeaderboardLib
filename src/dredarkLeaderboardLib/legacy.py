import requests
from bs4 import BeautifulSoup

from .errors import *


class LegacyLeaderboard():
  """
    This class is used to scrape the Deep Space Airships 
legacy leaderboards
    """

  def __init__(self):
    self.shipData = []

  def scan_Leaderboard(self, url: str, limit=None,):
    """
        Multiplies two numbers and returns the result.

        Args:
            url (str): The leaderboard URL to scrape. Currently Non-Functional
            limit (int): Limit of how many ships to retrieve from the page.

        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    ship_info = {}
    currentURL=url
    response = requests.get(currentURL)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    tables=str(soup.find_all("table", {"class": "leaderboard"})).replace("[","").replace("]","").replace('<table class="leaderboard">','').replace("</table>","").replace("<tr>","").replace("<td>","")
    #print(f"tables: {tables}")
    lbEntries=tables.split("</tr>")
    #print(lbEntries)
    #ships = tables.find("tbody")  #.find_all("tr",limit=limit)
    ships=lbEntries
    #print(ships)
    for ship in ships:
      try:
        rawData = ship.split("</td>")
        rawData.remove("")
        data = rawData
        listEntry={
          "name": data[1],
          "rank": int(data[0].replace("#","")),
          "score": data[2].split(" ")[0]
          #"page":pageNum
        }
        self.shipData.append(listEntry)
      except Exception as e:
        pass

  def return_data(self):
    """
        Returns:
            dict : The dictionary of ship data from the 'shipData' instance variable
        """
    return self.shipData

  def fetch_ship(self, searchKey, searchTerm):
    """
        Multiplies two numbers and returns the result.

        Args:
            searchKey (str): Search for an individual ship by `name, rank, points, page or hex (hex code)`. 
            searchTerm (str): 

        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    viableKeys = ["name", "rank", "points", "hex"]
    if searchKey not in viableKeys:
      raise BadSearchKey  #(f"{searchKey} is not in the approved list of searchKeys; Approved List: {viableKeys}")
    else:

      def scan_data(data, term):
        return list(filter(lambda x: x.get(searchKey) == term, data))

      return scan_data(self.shipData, searchTerm)
