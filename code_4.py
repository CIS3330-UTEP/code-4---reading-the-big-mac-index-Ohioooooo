import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
data_frame = pd.read_csv(big_mac_file)
country_code = "MEX"

def get_big_mac_price_by_year(year, country_code): 
    query_str = "(iso_a3 == '{country_code}') & (data_frame['date'].dtyear == {year})"
    mex_df = data_frame.query(query_str)
    return round(mex_df['dollar_price'].mean(), 2)

year = 2022
print(get_big_mac_price_by_year(year, country_code))

def get_big_mac_price_by_country(country_code):
    query_str = f"(iso_a3 == '{country_code.lower})"
    mex_df = df.search(query_str)
    return round(mex_df['dollar_price'].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

#def get_the_most_expensive_big_mac_price_by_year(year):
    #pass # Remove this line and code your function

if __name__ == "__main__":
    year = 2022 
    print(get_big_mac_price_by_year(year, country_code))
    