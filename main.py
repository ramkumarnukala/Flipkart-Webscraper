from bs4 import BeautifulSoup
import pandas as pd
import requests

ProductListLink = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

def main():
    page = requests.get(ProductListLink)
    soup = BeautifulSoup(page.content, "lxml")
    
    for item in soup.find_all("div", attrs={"class":"_1AtVbE"}):
        print(item.prettify())

if __name__=="__main__":
    main()