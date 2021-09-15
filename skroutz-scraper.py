import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

index = ['τεχνολογία', 'σπίτι-κήπος', 'μόδα', 'hobby-αθλητισμός',
         'υγεία-ομορφιά', 'παιδικά-βρεφικά', 'Auto - Moto', 'Επαγγελματικά - B2B']

categories = {}
categories['τεχνολογία'] = {}
categories['σπίτι-κήπος'] = {}
categories['μόδα'] = {}
categories['hobby-αθλητισμός'] = {}
categories['υγεία-ομορφιά'] = {}
categories['παιδικά-βρεφικά'] = {}
categories['Auto - Moto'] = {}
categories['Επαγγελματικά - B2B'] = {}

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.skroutz.gr/')
html = driver.page_source
'''
URL = 'https://www.skroutz.gr'
page = requests.get(URL)
soup = BeautifulSoup(page.content, features="html.parser")
time.sleep(3)
# print(soup.prettify())
i = 0
for a in soup.find_all('a', class_=None, href=True):
    if a['href'].find('/c/') != -1:
        URL = 'https://www.skroutz.gr' + a['href']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        time.sleep(3)

        for a2 in soup.find_all('a', class_='pic', href=True):
            if len(a2['class']) == 1:
                categories[index[i]][a2['title']] = {}
                URL = 'https://www.skroutz.gr/' + a2['href']

                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                time.sleep(3)

                for a3 in soup.find_all('a', class_='pic', href=True):
                    if len(a2['class']) == 1:
                        categories[index[i]][a2['title']][a3['title']] = {}
                        URL = 'https://www.skroutz.gr' + a3['href']

                        page = requests.get(URL)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        time.sleep(3)

                        for a4 in soup.find_all('div', class_='filter-group'):
                            if len(a4['class']) == 1:
                                categories[index[i]][a2['title']][a3['title']][a4.find(
                                    'div').find('h3').find('button')['title']] = {}
                                print(categories)
                                break
                    break
            break
    break

    # for a5 in a4.ul.li.find_all('a', class_='filter-option'):
    #    categories[index[i]][a2['title']][a3['title']
    #                                      ][a4.div.h3.button['title']][a5['title']] = {}

    i += 1
