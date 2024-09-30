import requests
from bs4 import BeautifulSoup

from .errors import *
from .checks import *


class Leaderboard():
  """
    This class is used to scrape the Deep Space Airships leaderboards
    """

  def __init__(self):
    self.shipData = []
    self.category = None
    self.bs4Soup = None

  @linkCheck("base")
  def scan_Leaderboard(self, url: str, totalPages=None, perPageLimit=None, totalLimit=None):
    """
        Scrapes the DSA leaderboard provided

        Args:
            url (str): The leaderboard URL to scrape.
            totalPages (int): The total number of pages for the leaderboard. (The number below the table). Default is None
            perPageLimit (int): Limit of how many entries to retrieve from each page.
            totalLimit (int): Limit of how many total entries to fetch.

        Returns:
            Nothing. The scanned data is stored in the 'shipData' instance variable.
        """
    if url.count("ship") > 0:
      self.category = "ships"
    elif url.count("pilot") > 0:
      self.category = "pilot"
    elif url.count("clan") > 0:
      self.category = "clan"
    pageNum=1
    shipCount=0
    ship_info = {}
    currentURL=url
    endLoopCheck=False #Check to end loop on last page when totalPages is none.
    last3Entries=[] #Last 3 entries to compare against to break loop when totalPages is none.
    while ((totalPages is not None) and (pageNum<totalPages)) or ((totalPages is None) and (endLoopCheck is False)):
      response = requests.get(currentURL)
      soup = BeautifulSoup(response.text, 'html.parser')
      self.bs4Soup=soup
      tables=str(soup.find_all("table", {"class": "leaderboard"})).replace("[","").replace("]","").replace('<table class="leaderboard">','').replace("</table>","").replace("<tr>","").replace("<td>","")
      lbEntries=tables.split("</tr>")
      if type(perPageLimit) is int:
        ships=lbEntries[:perPageLimit]
      else:
        ships=lbEntries
      if last3Entries==lbEntries[:3]:
        endLoopCheck=True
        break
      else:
        last3Entries=lbEntries[:3]
      for ship in ships:
        try:
          rawData = ship.split("</td>")
          rawData.remove("")
          data = rawData
          listEntry={}
          if url.count("ship")>0:
            listEntry={
              "name": data[1],
              "hex": data[2],
              "rank": int(data[0].replace("#","")),
              "score": int(data[3].split(" ")[0].replace(",",""))
            }
          elif url.count("pilot")>0:
            listEntry={
              "name": data[1],
              "rank": int(data[0].replace("#","")),
              "score": int(data[2].split(" ")[0].replace(",",""))
            }
          elif url.count("clan")>0:
            listEntry={
              "name": data[1],
              "rank": int(data[0].replace("#","")),
              "score": int(data[2].split(" ")[0].replace(",",""))
            }
          self.shipData.append(listEntry)
        except Exception as e:
          pass
      pageNum+=1
      currentURL=f"{url}&p={pageNum}"
    if type(totalLimit) is int:
      self.shipData=self.shipData[:totalLimit]



  def return_data(self):
    """
        Returns:
            dict : The dictionary of ship data from the 'shipData' instance variable
        """
    return self.shipData

  def fetch_ship(self, searchKey, searchTerm):
    """
        Fetches entries based on the key and term
        Viable Key: name, rank, points, hex

        Args:
            searchKey (str): Search for an individual ship by `name, rank, points, or hex (ship hex code)`. 
            searchTerm (str): The wanted term

        Returns:
            All Entries Matching The searchTerm & searchKey
        """
    viableKeys = ["name", "rank", "score", "hex"]
    if searchKey not in viableKeys:
      raise BadSearchKey
    else:

      def scan_data(data, term):
        return list(filter(lambda x: x.get(searchKey) == term, data))

      return scan_data(self.shipData, searchTerm)

  def fetch_ranks(self, start : int,  end : int, startInclusive=True, endInclusive=True):
    """
        Fetches ranks within the designated start-end range.

        Args:
            start (int): The rank at the start of the range
            end (int): The rank at the end of the range
            startInclusive: Default is True; if False, the start is not included in the list
            endInclusive: Default is True; if False, the end is not included in the list

        Returns:
            A List Of Entries Within The Specified Rank Range
        """
    def scan_data(data):
      if startInclusive and endInclusive:
        return list(filter(lambda x: (x.get("rank") >= start and x.get("rank") <= end) , data))
      elif startInclusive and not endInclusive:
        return list(filter(lambda x: (x.get("rank") >= start and x.get("rank") < end) , data))
      elif endInclusive and not startInclusive:
        return list(filter(lambda x: (x.get("rank") > start and x.get("rank") <= end) , data))
      else:
        return list(filter(lambda x: (x.get("rank") > start and x.get("rank") < end) , data))

    return scan_data(self.shipData)

  def search_by(self, key : str):
    """
        Searches for entries with names that contain the provided key.

        Args:
            key (str): The substring to search for in all entries.

        Returns:
            All entries that contain the specified key (substring).
    """
    return list(filter(lambda x: (x.get("name")).count(key) > 0, self.shipData))
