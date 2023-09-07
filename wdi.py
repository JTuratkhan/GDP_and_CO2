#imported all packges
import pandas as pd
import matplotlib.pyplot as plt

#importing csv file into dataframe
df = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
#create a scatter plot
df.plot.scatter(x="Mortality rate, infant (per 1,000 live births)", y="GDP per capita (constant 2010 US$)")
#print the plot
print(plt.show())
