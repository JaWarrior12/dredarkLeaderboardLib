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
    self.bs4Soup=None

  def scan_Leaderboard(self, url: str, totalPages=10, limit=None):
    """
        Scrapes the DSA leaderboard provided

        Args:
            url (str): The leaderboard URL to scrape.
            totalPages (int): The total number of pages for the leaderboard. (The number below the table). Default is 10 
            limit (int): Limit of how many ships to retrieve from the page.

        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    pageNum=1
    shipCount=0
    ship_info = {}
    currentURL=url
    while pageNum<totalPages:
      response = requests.get(currentURL)
      soup = BeautifulSoup(response.text, 'html.parser')
      self.bs4Soup=soup
      tables=str(soup.find_all("table", {"class": "leaderboard"})).replace("[","").replace("]","").replace('<table class="leaderboard">','').replace("</table>","").replace("<tr>","").replace("<td>","")
      lbEntries=tables.split("</tr>")
      ships=lbEntries
      for ship in ships:
        try:
          rawData = ship.split("</td>")
          rawData.remove("")
          data = rawData
          listEntry={
            "name": data[1],
            "rank": int(data[0].replace("#","")),
            "score": data[2].split(" ")[0]
          }
          self.shipData.append(listEntry)
        except Exception as e:
          pass
      pageNum+=1
      currentURL=f"{url}&p={pageNum}"

  def return_data(self):
    """
        Returns:
            dict : The dictionary of ship data from the 'shipData' instance variable
        """
    return self.shipData

  def fetch_ship(self, searchKey, searchTerm):
    """
        Fetches entries based on the key and term
        Viable Keys: name, rank, points

        Args:
            searchKey (str): Search for an individual ship by `name, rank, points`. 
            searchTerm (str): 

        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    viableKeys = ["name", "rank", "points"]
    if searchKey not in viableKeys:
      raise BadSearchKey
    else:

      def scan_data(data, term):
        return list(filter(lambda x: x.get(searchKey) == term, data))

      return scan_data(self.shipData, searchTerm)
