import requests
link = input("Enter wiki link : ")
url=requests.get(link).text
from bs4 import BeautifulSoup
soup=BeautifulSoup(url,'html.parser')
print("\nTitle of web page:",soup.title.string)
print(soup.find_all('a'))
for link in soup.find_all('a'):
    print(link.get('href'))