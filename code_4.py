import csv 
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv("big-mac-full-index.csv")


def get_big_mac_price_by_year(year,country_code): 
    data = df.query(f"'{year}-01-01' <= date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}'")
    return round(data['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    data = df.query(f"iso_a3 == '{country_code.upper()}'")
    return round(data['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    data = df.query(f"'{year}-01-01' <= date <= '{year}-12-31'")
    cheapest = data.loc[data['dollar_price'].idxmin()]
    return f"{cheapest['name']} ({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    data = df.query(f"'{year}-01-01' <= date <= '{year}-12-31'")
    expensive = data.loc[data['dollar_price'].idxmax()]
    return f"{expensive['name']} ({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    year = int(input("Enter year: ").strip())
    country_code = input("Enter the country code (lowercase): ").strip().lower()
    print(get_big_mac_price_by_year(year, country_code))
    print(get_big_mac_price_by_country(country_code))
    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))
          