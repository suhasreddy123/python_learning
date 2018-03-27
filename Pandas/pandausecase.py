import pandas as pd
import numpy as np
df=pd.read_csv("/home/ramesh/Documents/results.csv")
df["home_team_wins"]=df.home_score > df.away_score
df["away_team_wins"]=df.home_score < df.away_score
df["Team_draws"]=df.home_score == df.away_score
"""print(df.head())
a=df[df.home_team_wins==True].count().home_team_wins
b=df[df.away_team_wins==True].count().away_team_wins
c=df[df.Team_draws==True].count().Team_draws
print("wins of the home_team",a)
print("wins of the away_team",b)
print("draw matches",c)"""
print("wins of home team",df.home_team_wins.sum())
print("wins of home team",df.away_team_wins.sum())
print("wins of home team",df.Team_draws.sum())
"""total=(a+b+c)
print("losses of the home_team",total-(c+a))
print("losses of away team",total-(c+b))
print(df.head())"""
in_2018=df.date>="2018"
print("In 2018 home team wins are",df[in_2018]["home_team_wins"].sum())
print("In 2018 away team wins are",df[in_2018]["away_team_wins"].sum())
