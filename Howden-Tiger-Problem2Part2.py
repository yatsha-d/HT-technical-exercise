import pandas as pd
df = pd.read_csv('Currency_rates_to_gbp.csv') # read in the csv

average_rate = df['Rate to GBP'].mean() # get the average of the conversion rates

highest_value_against_GBP = df.loc[df['Rate to GBP'].idxmax()] # get the maximum conversion rate
lowest_value_against_GBP = df.loc[df['Rate to GBP'].idxmin()] # get the minimum conversion rate

comparative_analysis = pd.DataFrame({
    'Metric': ['Average Conversion Rat to GBP', 'Highest Value Against GBP', 'Lowest Value Against GBP'], # create a column to house the metrics
    'Values': [average_rate, f"{highest_value_against_GBP['Currency']} ({highest_value_against_GBP['Rate to GBP']})", # create a column to house the different rates
               f"{lowest_value_against_GBP['Currency']} ({lowest_value_against_GBP['Rate to GBP']})"]
})

comparative_analysis.to_csv('Currency_conversion_analysis.csv', index=False) # output the analysis to a csv
