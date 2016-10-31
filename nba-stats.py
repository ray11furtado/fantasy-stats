import bs4 
from datetime import datetime 
import requests
import pandas as pd 
from pandas import DataFrame

class nba:
  def __init__(self, start_day, days):
    self.start = str(start_day)
    self.days = days
    self.indexs = ['Name', '3PM', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'Points']
    self.df = DataFrame(index = self.indexs)

  def getData(self, minmum_mins):
    counter = 0
    while counter <= self.days:
      self.url = "http://games.espn.com/fba/leaders?&scoringPeriodId="+self.start+"&seasonId=2017"
      self.res = requests.get(self.url).text
      self.soup = bs4.BeautifulSoup(self.res, 'lxml')
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
        print player_name

        if minmum_mins:
          if minutes > minmum_mins:
            stats = [player_name, threes, rebounds, assists, steals, blocks, points]
            df_holder = DataFrame(stats, index =self.indexs)
            self.df = self.df.append(df_holder)
        else:
          stats = [player_name, threes, rebounds, assists, steals, blocks, points]
          df_holder = DataFrame(stats, index =self.indexs)
          self.df = self.df.append(df_holder)
      next_day = int(self.start) + 1
      self.start = str(next_day)
      counter += 1

  def writeToCsv(self, name):
    name = name + '.csv'
    self.df.to_csv(name, index=self.indexs)


kobe = nba(1,1)
kobe.getData(20)
kobe.writeToCsv('text')