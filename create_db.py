from bs4 import BeautifulSoup
from bs4.builder import _lxml
import requests

url = 'http://euroleaguebasketball.net/el/euroleague/stats/expanded/?size=1000&viewType=traditional&fromSeasonCode=E2025&toSeasonCode=E2025&statisticMode=perGame&seasonMode=Range&sortDirection=descending&statistic=valuation'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

print(soup)
