import requests
from bs4 import BeautifulSoup
import re
URL = "https://www.cursbnr.ro/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
soup.prettify()


table = soup.find('div', attrs = {'class':'table-responsive'})
data_curs=table.find('th', attrs = {'colspan':'2'}).text
print("Cursul BNR comunicat în data de: ",data_curs)


table2=table.find('tbody')
data=[]
for row in table2.findAll('td', attrs={'class':"text-center"}):
    r1=re.compile("[A-Z]")
    r2=re.compile("[0-9].[0-9]")
    if r1.match(row.text):
          data.append(row.text)
    else:
        if r2.match(row.text):
          data.append(row.text)

i=2
while i <= len(data):
    data[i]=0;
    data[i+1]=0;
    i=i+4

for i in data:
    data.remove(0)
i=1
while i<= len(data):
    data[i]=float(data[i])
    i=i+2


data=[tuple(data[i: i + 2]) for i in range(0, len(data), 2)]
print(data)
















