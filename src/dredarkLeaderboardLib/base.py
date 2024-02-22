import requests
from bs4 import BeautifulSoup

from .errors import *


class Leaderboard():
  """
    This class is used to scrape the Deep Space Airships leaderboards
    """

  def __init__(self):
    self.shipData = []

  def scan_Leaderboard(self, url: str, limit=None):
    """
        Scrapes the DSA leaderboard provided
    
        Args:
            url (str): The leaderboard URL to scrape.
            limit (int): Limit of how many ships to retrieve from the page.
    
        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    ship_info = {}
    if url.count("ship")>=1:
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      tables=str(soup.find_all("table", {"class": "leaderboard"})).replace("[","").replace("]","").replace('<table class="leaderboard">','').replace("</table>","").replace("<tr>","").replace("<td>","")
      lbEntries=tables.split("</tr>")
      ships=lbEntries
      for ship in ships:
        try:
          rawData = ship.split("</td>")
          rawData.remove("")
          data = rawData
          listEntry={
            "hex": data[1],
            "rank": int(data[0].replace("#","")),
            "score": data[2].split(" ")[0]
          }
          self.shipData.append(listEntry)
        except Exception as e:
          pass
    elif url.count("pilot")>=1:
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
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
    elif "clan" in url:
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      tables=str(soup.find_all("table", {"class": "leaderboard"})).replace("[","").replace("]","").replace('<table class="leaderboard">','').replace("</table>","").replace("<tr>","").replace("<td>","")
      lbEntries=tables.split("</tr>")
      ships=lbEntries
      for ship in ships:
        try:
          rawData = ship.split("</td>")
          rawData.remove("")
          data = rawData
          listEntry={
            "clan": data[1],
            "rank": int(data[0].replace("#","")),
            "score": data[2].split(" ")[0]
          }
          self.shipData.append(listEntry)
        except Exception as e:
          pass
    else:
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
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

  def return_data(self):
    """
        Returns:
            dict : The dictionary of ship data from the 'shipData' instance variable
        """
    return self.shipData

  def fetch_ship(self, searchKey, searchTerm):
    """
        Fetches entries based on the key and term
    
        Args:
            searchKey (str): Search for an individual ship by `name, rank, points, or hex (hex code)`. 
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
