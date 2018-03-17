import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={"year":[2010,2011,2012,2011,2012,2010,2011,2012],
      "team":['bears',"bears","bears","packers","beams","lions","lions","bears"],
      "wins":[11,8,9,10,5,11,6,12],
      'losses':[5,8,6,1,5,10,6,12]}
football=pd.DataFrame(data,columns=["year","team","wins","losses"])
print(football)