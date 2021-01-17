import requests
from bs4 import BeautifulSoup

URL = 'https://www.startupdetector.de/neue-startups/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

import csv
html = open("https://www.startupdetector.de/neue-startups/").read()
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
