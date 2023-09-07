import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
df.plot.scatter(x="Mortality rate, infant (per 1,000 live births)", y="GDP per capita (constant 2010 US$)")
print(plt.show())
