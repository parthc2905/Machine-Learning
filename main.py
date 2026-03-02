#fetch data from a website
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "https://www.youtube.com/watch?v=4HyTlbHUKSw&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH&index=24"
response = requests.get(url,headers=headers) # getting data
print(response.text)