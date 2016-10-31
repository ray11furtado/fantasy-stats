import bs4 
from datetime import datetime 
import requests
import pandas as pd 
from pandas import DataFrame

class nba:
  def __init__(self, start_day, days):
    self.start = str(start_day)
    self.indexs = ['Name', '3PM', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'Points', 'Fantasy_Points']
    self.df = DataFrame(index = self.indexs)

  def getData(self, minmum_mins):
    counter = 0
    while counter <= self.days:
      self.url = "http://games.espn.com/fba/leaders?&scoringPeriodId="+self.start+"&seasonId=2017"
      self.res = requests.get(self.url).text
      self.soup = bs4.BeautifulSoup(self.res, 'html.parser')
      table = self.soup.find(("table", {"class" : "playerTableTable tableBody"}))

      for row in table.findAll('tr')[3:]:
        col = row.findAll('td')
        player_name = col[0].a.string.strip()
        minutes = col[5].string.strip()
        threes = col[10].string.strip()
        rebounds = col[11].string.strip()
        assists = col[12].string.strip()
        steals = col[13].string.strip()
        blocks = col[14].string.strip()
        points = col[15].string.strip()

        if minmum_mins:
          if Minutes > minmum_mins:
            stats = [player_name, threes, rebounds, assists, steals, blocks,point]
            df_holder = DataFrame(stats, index =self.indexs)
            self.df1 = self.df1.append(df2)
        else:
          stats = [player_name, threes, rebounds, assists, steals, blocks,point]
          df_holder = DataFrame(stats, index =self.indexs)
          self.df1 = self.df1.append(df2)
      self.days += 1
      counter += 1

  def writeToCsv(self, name):
    name = name + '.csv'
    self.df1.to_csv(name, index=self.indexs)


