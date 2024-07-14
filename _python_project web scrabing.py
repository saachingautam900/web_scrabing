from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup

soup = BeautifulSoup(soup.text, "lxml")
soup = soup.table

data = []
tags = soup.find_all('tr')
for i in tags:
  y = i.text.split('\n')[1:]
  if y[0] != '':
    data.append(y)

data

import csv
file = open('covid.csv','w')
x = csv.writer(file)
x.writerows(data)
file.close()

pwd

import pandas as pd
df = pd.read_csv('covid.csv',encoding = 'latin1')
df

df = df[0:10]

TotalCases = [int(i.replace(',','')) for i in df['TotalCases']]
Country = df['Country,Other']

print(TotalCases)

# !pip install plotly==5.20.0

import plotly.graph_objects as go
fig = go.Figure([go.Bar(x=Country, y=TotalCases)])
fig.show()

import plotly.graph_objects as go
TotalDeath = [int(i.replace(',','')) for i in df['TotalDeaths']]
TotalCases = [int(i.replace(',','')) for i in df['TotalCases']]
Country = df['Country,Other']
fig = go.Figure(data=[
    go.Bar(name='Total Cases', x=Country, y=TotalCases),
    go.Bar(name='Total Death', x=Country, y=TotalDeath)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

import pandas as pd
df = pd.read_csv('covid.csv',encoding = 'latin1',index_col = 'Country,Other')
df1 = df.loc['USA':'Brazil']
country = df1.index.values
country

df1['TotalCases'].values

