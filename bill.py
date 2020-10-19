from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from selenium import webdriver
from time import sleep 
import openpyxl as xl 

PATH = '/home/lukas/Documents/drivers/chromedriver'

def parse(url):
    response = webdriver.Chrome(PATH)
    response.get(url)
    sleep(3)
    sourceCode = response.page_source
    return sourceCode


hnb_page = soup(parse("https://www.hnb.hr/temeljne-funkcije/monetarna-politika/tecajna-lista/tecajna-lista"), "lxml")

table = hnb_page.findAll("tr")
emu = table[13]
values = emu.findAll("td", {"class":"cell_right"})
value = values[1].text

wb = xl.load_workbook('/home/lukas/Documents/Programming/Python/ProjectBill/test.xlsx')
sheet = wb['List1']
cellFix = sheet['l16']
cellFix.value = value
wb.save('/home/lukas/Documents/Programming/Python/ProjectBill/test.xlsx')
print(cellFix.value)
