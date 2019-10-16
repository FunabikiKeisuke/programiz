from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

html_doc1 = requests.get("https://www.hayamihyo.com/todohuken/").text
html_doc2 = requests.get("https://www.stat.go.jp/naruhodo/c1data/02_01_stt.html").text
html_doc3 = requests.get("https://region-case.com/list-special-product/").text
html_doc4 = requests.get("https://www.teikokushoin.co.jp/statistics/japan/index01.html").text
soup1 = BeautifulSoup(html_doc1, 'html.parser')
soup2 = BeautifulSoup(html_doc2, 'html.parser')
soup3 = BeautifulSoup(html_doc3, 'html.parser')
soup4 = BeautifulSoup(html_doc4, 'html.parser')

datas1 = soup1.find_all("td", {"class": "td1"})
datas2 = soup1.find_all("td", {"class": "td2"})
datas3 = soup2.find_all("td", {"class": "txtr"})
datas4 = soup3.find_all("td")
datas5 = soup4.find_all("td", {"align": "right"})

columns = ["prefecture", "capital", "population", "local_specialty", "area"]
df = pd.DataFrame(columns=columns)

n = 0
for data1 in datas1:
    prefecture = data1.string
    i = 0
    for data2 in datas2:
        if i == n:
            capital = data2.string
        i = i+1
    j = 0
    for data3 in datas3:
        if j == (n+1):
            population = data3.string
            population = population.replace(",", "")
        j = j+1
    k = 0
    for data4 in datas4:
        if k == n:
            local_specialty = data4.string
        k = k+1
    l = 0
    for data5 in datas5:
        if l == (n+2):
            area = data5.string
            area = area.replace(",", "")
        l = l+1
    n = n+1
    se = pd.Series([prefecture, capital, population, local_specialty, area], columns)
    df = df.append(se, columns)

filename = "prefecture.csv"
df.to_csv(filename, encoding='utf-8-sig', index=None)
