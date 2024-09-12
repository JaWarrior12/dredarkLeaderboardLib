import src.dredarkLeaderboardLib as dll
from src.dredarkLeaderboardLib.checks import *

import unittest
import requests
#import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
#from import Leaderboard

SEASON=1
CATEGORY="bots"
KEY="p"
LIMIT=10
TOTALPAGES=10

class TestArchiveLeaderboard(unittest.TestCase):
    def setUp(self):
        self.statistics = dll.ArchiveLeaderboard()

    @patch('src.dredarkLeaderboardLib.archive.requests.get')
    @patch('src.dredarkLeaderboardLib.archive.BeautifulSoup')
    def test_scan_Leaderboard(self, mock_bs, mock_requests_get):
        mock_requests_get.return_value = MagicMock()
        mock_bs.return_value = BeautifulSoup("", 'html.parser')
        self.statistics.scan_Leaderboard(SEASON, CATEGORY, KEY, TOTALPAGES, LIMIT)
        self.assertTrue(self.statistics.shipData)

    def test_return_data(self):
        self.statistics.shipData = [{"name": "JaMWarrior", "rank": 1, "score": 1000}]
        self.assertEqual(self.statistics.return_data(), self.statistics.shipData)

    def test_fetch_ship(self):
        self.statistics.shipData = [{"name": "JaMWarrior", "rank": 1, "score": 1000}]
        self.assertEqual(self.statistics.fetch_ship("name", "JaMWarrior"), [{"name": "JaMWarrior", "rank": 1, "score": 1000}])

        with self.assertRaises(BadSearchKey):
            self.statistics.fetch_ship("invalid_key", "JaMWarrior")

    def test_fetch_ranks(self):
        self.statistics.shipData = [
            {"name": "JaMWarrior", "rank": 1, "score": 1000},
            {"name": "ReplAI", "rank": 2, "score": 900}
        ]

        self.assertEqual(self.statistics.fetch_ranks(1, 2, True, True), [
            {"name": "JaMWarrior", "rank": 1, "score": 1000},
            {"name": "ReplAI", "rank": 2, "score": 900}
        ])

if __name__ == '__main__':
    unittest.main()