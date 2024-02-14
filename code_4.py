import csv
import pandas as pd
df = pd.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year, country_code): 
    country = f"(iso_a3 == '{country_code.upper()}' and date.str.contains('{year}'))"
    by_year = df.query(country)
    return round(by_year['dollar_price'].mean(),2)

def get_big_mac_price_by_country(country_code):
    country = f"(iso_a3 == '{country_code.upper()}')"
    by_country = df.query(country)
    return round(by_country['dollar_price'].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    date_year = f"(date.str.contains('{year}'))"
    by_year = df.query(date_year)
    minimum_ = by_year['dollar_price'].idxmin()
    min_ = by_year.loc[minimum_]
    return f"{min_['name']}({min_['iso_a3']}): ${round(min_['dollar_price'],2)}"
    
def get_the_most_expensive_big_mac_price_by_year(year):
    price_year = f"(date.str.contains('{year}'))"
    by_year = df.query(price_year)
    maximum_ = by_year['dollar_price'].idxmax()
    max_ = by_year.loc[maximum_]
    return f"{max_['name']}({max_['iso_a3']}): ${round(max_['dollar_price'],2)}"

if __name__ == "__main__":
    x = get_big_mac_price_by_year(2003, "by")
    print(x)
    x = get_big_mac_price_by_country ("by")
    print(x)
    x = get_the_cheapest_big_mac_price_by_year(2005)
    print(x)
    x = get_the_most_expensive_big_mac_price_by_year(2005)
    print(x)


    

