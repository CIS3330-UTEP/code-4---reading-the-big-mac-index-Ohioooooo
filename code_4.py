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
    
def get_big_mac_price_by_country(country_code):
    results = []
    for i,r in df.iterrows():
        country_name = str(r['name']).lower()
        mean_price = round(float(r['dollar_price']),2)
        print(country_name, mean_price)

def get_the_cheapest_big_mac_price_by_year(year):
    results = []
    for i,r in df.iterrows():
        year_str = str((r['date']))
        country_code = str(r['iso_a3']).lower()
        country_name = str(r['name'])
        mean_price = round(float(r['dollar_price']))
        results.append((country_name ,country_code, mean_price))
    min_price_tuple = min(results, key=lambda x: x[2])
    return min_price_tuple

def get_the_most_expensive_big_mac_price_by_year(year):
    results = []
    for i,r in df.iterrows():
        year_str = str((r['date']))
        country_code = str(r['iso_a3']).lower()
        country_name = str(r['name'])
        mean_price = round(float(r['dollar_price']))
        results.append((country_name ,country_code, mean_price))
    max_price_tuple = max(results, key=lambda x: x[2])
    return max_price_tuple

if __name__ == "__main__":
    year = 'date'
    country_code = 'iso_a3'
    print(get_big_mac_price_by_year(year, country_code))

    print(get_big_mac_price_by_country(country_code))

    print(get_the_cheapest_big_mac_price_by_year(year))

    print(get_the_most_expensive_big_mac_price_by_year(year))


    

