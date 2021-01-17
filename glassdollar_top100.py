import requests
from bs4 import BeautifulSoup

URL = 'https://glassdollar.com/top-100-startups-germany'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

import csv
html = open("https://glassdollar.com/top-100-startups-germany").read()
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
    
    
