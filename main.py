from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("D:\Pobrane\chromedriver_win32\chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
driver.get('https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq')


content = driver.page_source
# print(content)
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')