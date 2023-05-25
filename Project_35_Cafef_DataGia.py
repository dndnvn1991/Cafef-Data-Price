import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


#Đọc từng dòng trong file txt - Trả về 1 list
with open('Project_35_Cafef_Datalink.txt','r') as file:
     content = file.readlines()
     print(content)

stock_list = []
for link in content:    
    url = link[:-1]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find_all('div', class_='dltlu-point')[0].text.strip()
    try:
        if soup.find('div', {'id':'symbolbox'}): 
            symbol = soup.find('div', {'id':'symbolbox'}).text.strip()
        else:
            symbol = soup.find('div', {'class':'symbol'}).text.strip()
    except:
        symbol = 'NaN'
    stock = {
            'Symnbol': symbol,
            'price' :  price        
    }
    stock_list.append(stock)
    print(stock)

df =  pd.DataFrame(stock_list)
print(df.head(10))
df.to_csv('Project_35_DataGia.csv')

#Báo cáo - Report
print('Total Links: ', len(content))
print('Total Stock Scaping: ',len(df))
