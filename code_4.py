import csv
import pandas as pd
df = pd.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year, country_code): 
    results = []
    for i,r in df.iterrows():
        year_str = str(r['date'])
        country_code_lower = str(r['iso_a3']).lower()
        mean_price = round (float(r['dollar_price']),2)
        print(year_str, country_code_lower, mean_price)
    
#def get_big_mac_price_by_country(country_code):
    #query_str = f"(iso_a3 == '{country_code.lower})"
    #mex_df = df.search(query_str)
    #return round(mex_df['dollar_price'].mean(),2)

#def get_the_cheapest_big_mac_price_by_year(year):
    #pass # Remove this line and code your function

#def get_the_most_expensive_big_mac_price_by_year(year):
    #pass # Remove this line and code your function

if __name__ == "__main__":
    year = 'date'
    country_code = 'iso_a3'
    print(get_big_mac_price_by_year(year, country_code))