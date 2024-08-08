
# # Webscraping in Python 

from bs4 import BeautifulSoup
import requests

# GET request
url = 'https://en.wikipedia.org/wiki/California_locations_by_crime_rate'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)


table0 = soup.find_all('table')[0]
print(table0)


table1 = soup.find_all('table')[1]
print(table1)


table2 = soup.find_all('table')[2]
print(table2)


table1col = table1.find_all('th')
print(table1col)


table1columns = [title.text.strip() for title in table1col]
print(table1columns)


#remove brackets & stuff inside
import re
def remove_brackets(text):
    return re.sub(r'\[.*?\]', '', text).strip()

# Cleaned column titles
table1columns = [remove_brackets(title) for title in table1columns]

table1columns

table2col = table2.find_all('th')
print(table2col)

table2columns = [title.text.strip() for title in table2col]
print(table2columns)

#remove brackets
def remove_brackets(text):
    return re.sub(r'\[.*?\]', '', text).strip()

# Cleaned column titles
table2columns = [remove_brackets(title) for title in table2columns]
print(table2columns)

import pandas as pd 

df1 = pd.DataFrame(columns = table1columns)
df1

df2 = pd.DataFrame(columns = table2columns)
df2

col1 =  table1.find_all('tr')
print(col1)


for row in col1[1:]:
    row1 = table1.find_all('td')
    row1data = [data.text.strip() for data in row1]
print(row1data)

for i in range(0, len(row1data), 7):
    chunk = row1data[i:i+7]
    if len(chunk) == 7:
        df1.loc[len(df1)] = chunk

#Remove commas
    df1 = df1.replace(',','',regex=True)

print(df1)

df2

col2 =  table2.find_all('tr')

for row in col2[1:]:
    row2 = table2.find_all('td')
    row2data = [data.text.strip() for data in row2]
print(row2data)

print(df2)



for i in range(0, len(row2data), 8):
    chunk = row2data[i:i+8]
    if len(chunk) == 8:
        df2.loc[len(df2)] = chunk
df2 = df2.replace(',','',regex=True)

print(df2)

df2

df1


print(df1.dtypes)


df1['County'] = df1['County'].astype('category')
df1['Population'] = pd.to_numeric(df1['Population'], errors='coerce')
df1['Populationdensity'] = pd.to_numeric(df1['Populationdensity'], errors='coerce')
df1['Violent crimes'] = pd.to_numeric(df1['Violent crimes'], errors='coerce')
df1['Violent crime rateper 1,000 persons'] = pd.to_numeric(df1['Violent crime rateper 1,000 persons'], errors='coerce')
df1['Property crimes '] = pd.to_numeric(df1['Property crimes'], errors='coerce')
df1['Property crime rateper 1,000 persons'] = pd.to_numeric(df1['Property crime rateper 1,000 persons'], errors='coerce')
print(df1.dtypes)
df1_encoded = pd.get_dummies(df1, columns=['County'], drop_first=False)
df1_encoded = df1_encoded.astype(int)
print(df1_encoded)

print(df2.dtypes)


df2['City/Agency'] = df2['City/Agency'].astype('category')
df2['County'] = df2['County'].astype('category')
df2['Population'] = pd.to_numeric(df2['Population'], errors='coerce')
df2['Populationdensity'] = pd.to_numeric(df2['Populationdensity'], errors='coerce')
df2['Violent crimes'] = pd.to_numeric(df2['Violent crimes'], errors='coerce')
df2['Violent crime rateper 1,000 persons'] = pd.to_numeric(df2['Violent crime rateper 1,000 persons'], errors='coerce')
df2['Property crimes'] = pd.to_numeric(df2['Property crimes'], errors='coerce')
df2['Property crime rateper 1,000 persons'] = pd.to_numeric(df2['Property crime rateper 1,000 persons'], errors='coerce')
print(df2.dtypes)

df2_encoded = pd.get_dummies(df2, columns=['County','City/Agency' ], drop_first=False)
df2_encoded = df2_encoded.astype(int)
print(df2_encoded)

