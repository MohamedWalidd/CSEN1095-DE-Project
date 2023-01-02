import datetime
import numpy as np
import pandas as pd
def getWeekNumber(date, year):
  end_date = datetime.datetime(year, 12, 31)
  delta = end_date - date
  week = 0
  if(delta!=0):
    week = 52 - delta.days//7 +1
  return int(week)

def discretize_dates(dataframe):
  df = dataframe.copy()
  dates = df['date']
  weeks = np.zeros(len(dates))
  for i in range(len(dates)):
    if(pd.isnull(dates.iloc[i])):
      weeks[i]=0
    else:
      weeks[i] = getWeekNumber(dates.iloc[i],df.iloc[i]['accident_year'])
  df['week_number'] =  weeks
  return df       