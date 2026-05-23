import requests
from bs4 import BeautifullSoup


car=input("Enter the name : ")
url=f'https://www.pakwheels.com/{car}-for-sale'
response=requests.get(url)
if response.status_code==200:
    soup
