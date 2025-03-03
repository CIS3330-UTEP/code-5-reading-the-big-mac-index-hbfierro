import csv 
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df=big_mac_file


def get_big_mac_price_by_year(year,country_code): 
    date_find = round(df.loc[(df['year'] == year) & (df['iso_a3'].str.upper() == country_code), 'dollar_price'].mean(), 2)
    return date_find

def get_big_mac_price_by_country(country_code):
    dollar_price = round([df['iso_a3'].str.lower() == country_code, 'dollar_price'].mean(), 2)
    return dollar_price

def get_the_cheapest_big_mac_price_by_year(year):
    filtered_df = df[df['year'] == year].nsmallest(1, 'dollar_price')
    row = filtered_df.iloc[0]
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    row = df.loc[df['year'] == year].nlargest(1, 'dollar_price').iloc[0]
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"

if __name__ == "__main__":
    df= pd.read_csv('./big-mac-full-index.csv')
    year = int(input("Enter year: ").strip())
    country_code = input("Enter the country code (lowercase): ").strip().lower()
    print(get_big_mac_price_by_year(year, country_code))
    print(get_big_mac_price_by_country(country_code))
    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))
          