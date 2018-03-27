import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
df=pd.read_csv("/home/ramesh/Documents/results.csv")
df["home_team_wins"]=df.home_score > df.away_score
df["away_team_wins"]=df.home_score < df.away_score
df["Team_draws"]=df.home_score == df.away_score
#print(df.head())
print(df.groupby("country").home_team_wins.sum())
df['date'] = pd.to_datetime(df['date'])
print(df.date.dtype)
df['Date1'] = df['date'].dt.strftime('%Y')
df['Date1']=pd.to_numeric(df["Date1"])
print(df.groupby("Date1").home_team_wins.sum())
print(df)
r=df[(df.Date1>=1872)&(df.home_team_wins==True)]
print(r.head())
s=pd.crosstab(r.country,r.Date1)
#print(s.sum())

#s.to_csv('footballdata.csv', index=True)
#print(s.plot(kind="hist"))