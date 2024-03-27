import pandas as pd # in order to read in the csv
import matplotlib.pyplot as plt # in order to create visualisations

path = r'C:\Users\Yatsha\Documents\Python\HT technical exercise\Howden Tiger - Data.csv'
df = pd.read_csv(path) # read in the csv

sector_ebitda_avg = df.groupby('Sector')['Ebitda'].mean().sort_values(ascending=False) # calculate average EBITDA for each sector

highest_sector = sector_ebitda_avg.idxmax() # identify the sector with the highest average EBITDA
print(f"The sector with the highest average EBITDA is: {highest_sector}")

plt.figure(figsize=(10,10))
sector_ebitda_avg.plot(kind='bar') # create a bar chart
plt.title('Average EBITDA by Sector') # title of the chart
plt.ylabel('Average EBITDA') # y-axis title
plt.xlabel('Sector') # x-axis title
plt.xticks(rotation=45, ha='right') # to make it easier to read the x-axis values
plt.tight_layout() # to make the bar chart fit in the window
plt.show() # create a bar chart showing the data


technology = df[df['Sector'] == 'Technology'] # filter to the technology sector
avg_price_of_ce = technology[technology['Industry'] == 'Consumer Electronics']['Currentprice'].mean() # calculate average current price for consumer electronics
avg_price_of_si = technology[technology['Industry'] == 'Software-Infrastructure']['Currentprice'].mean() # calculate average current price for software infrastructure
print(f"The average current price for Consumer Electronics is: {avg_price_of_ce}") # return the average prices
print(f"The average current price for Software Infrastructure is: {avg_price_of_si}")# return the average prices

plt.figure(figsize=(10,10))
plt.bar(['Consumer Electronics', 'Software-Infrastructure'], [avg_price_of_ce, avg_price_of_si], color=['red', 'blue']) # create a bar chart of the two industries
plt.title('Average Current Price') # add a title
plt.ylabel('Average Current Price') # add a y-axis label
plt.show()

# Analysis
# Software Infrastructure has the higher average current price, this may indicate that thre is high demand for software services e.g cloud computing, data storage and software/cybersecurity
# Some companies within this industry are very big, with almost monopoly-like power e.g Microsoft, Adobe which enables these companies to command higher prices for their services
# Investors could be driving up the average current price due to confidence in the long-term growth potential i.e. if the companies are investing in R&D to follow trends in AI
# then investors might be willing to pay more for shares
