import requests
import bs4

result = requests.get("https://www.cricbuzz.com/live-cricket-scores/46066/lsg-vs-mi-37th-match-indian-premier-league-2022")

soup = bs4.BeautifulSoup(result.text , "lxml")

getTitle = soup.select('title')[0].getText()

print(getTitle)