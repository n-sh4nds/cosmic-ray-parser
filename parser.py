
# This is a data processing program that will extract and analyze cosmic ray data from the Oulu Cosmic Ray Station and then compute basic statistics.
# Data Source: This project uses data from the Oulu Cosmic Ray Station: https://cosmicrays.oulu.fi/

import pandas as pd

def main():
    cosmic_df = pd.read_csv("OULU_82026_92026.csv") # read data from CSV file and return pandas DataFrame

    cosmic_df.rename(columns={ # rename columns for better readability
        'FractionalDate': 'fractional_date',
        'UncorrectedCountRate[cts/min]': 'uncorrected_count_rate',
        'CorrectedCountRate[cts/min]': 'corrected_count_rate',
        'Pressure[mbar]': 'pressure'
    }, inplace=True)
    
    column_titles = (cosmic_df.columns) # assign column labels of the CSV to column_titles
    print("\nNumber of columns: ", len(column_titles)) # print the number of columns

    rows_count = len(cosmic_df) # extract the number of rows in the DataFrame using len()
    print("Number of rows: ", rows_count, "\n") # print the number of rows

    stats = cosmic_df.describe() # find count, mean, std, min, 25%, 50%, 75%, and max of all columns

    info = "Corrected Count Rate Statistics" # set title for CorrectedCountRate information 
    ccr_mean = stats.loc["mean", "corrected_count_rate"] # get CorrectedCountRate mean
    ccr_median = stats.loc["50%", "corrected_count_rate"] # get CorrectedCountRate median
    ccr_max = stats.loc["max", "corrected_count_rate"] # get CorrectedCountRate max 
    ccr_min = stats.loc["min", "corrected_count_rate"] # get CorrectedCountRate min

    print(info)
    print("-" * len(info)) 
    print("Mean:", ccr_mean) 
    print("Median:", ccr_median)
    print("Maximum:", ccr_max)
    print("Minimum:", ccr_min)

    def greater_than_mean(x): # create function that tests if a number is greater than the CorrectedCountRate mean
        if x > ccr_mean:
            return True
        else: return False

    cosmic_df["ccr_mean_check"] = cosmic_df["corrected_count_rate"].apply(greater_than_mean) # check all CorrectedCountRate values 

    count = (cosmic_df["ccr_mean_check"] == True).sum() # count the number of values that are greater than the mean

    print("\nThere are", count, "values greater than the mean.\n") # print result of greater_than_mean function
    
main()

