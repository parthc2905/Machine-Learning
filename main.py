import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=500"

response = requests.get(url,headers=agent)
# print(response.text)
soup = BeautifulSoup(response.text , 'lxml')
mydivs = soup.find_all('div', class_="companyCardWrapper")
import os
print(mydivs)
os.system('cls')
