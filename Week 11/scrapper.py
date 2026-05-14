import requests
from bs4 import BeautifulSoup


car=input("Enter name :")
url=f'https://www.pakwheels.com/new-cars/pricelist/{car}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
response=requests.get(url, headers=headers)


if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    tables=soup.find_all('table')
    if not tables:
        print("No tables found on the webpage.")
    for table in tables:
        rows=table.find_all('tr')
        for row in rows:
            cols=row.find_all('td')
            if len(cols)>= 2:
                name=cols[0].get_text()
                price=cols[1].get_text()
                print(f"Name: {name}, Price: {price}")
            
        
else:
    print("Failed to retrieve the webpage.")    


#create a function to scrape data from the webpage, the above code can be used inside the function
def scrapper():
    pass


# create a function to save data to a csv file
def save_to_file(data, filename):
    pass