import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json

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
URL = 'https://www.skroutz.gr/'
page = requests.get(URL)
html = page.content
soup = BeautifulSoup(html, features="html.parser")
# print(soup.prettify())
i = 0

for a in soup.find_all('a', class_=None, href=True):  # e.g. technology

    if a['href'].find('/c/') != -1:

        URL = 'https://www.skroutz.gr' + a['href']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        for a2 in soup.find_all('a', class_='pic', href=True):  # e.g. mobile
            if len(a2['class']) == 1:
                categories[index[i]][a2['title']] = {}
                URL = 'https://www.skroutz.gr/' + a2['href']
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')

                # e.g. mobile phones
                for a3 in soup.find_all('a', class_='pic', href=True):
                    if len(a2['class']) == 1:
                        categories[index[i]][a2['title']][a3['title']] = {}
                        URL = 'https://www.skroutz.gr' + a3['href']
                        page = requests.get(URL)
                        soup = BeautifulSoup(page.content, 'html.parser')

                        for a4 in soup.find_all('a',  class_='pic', href=True):
                            if len(a4['class'] == 1):
                                categories[index[i]][a2['title']
                                                     ][a3['title']][a4['title']] = {}
                                URL = 'https://www.skroutz.gr' + a4['href']
                                page = requests.get(URL)
                                soup = BeautifulSoup(
                                    page.content, 'html.parser')

                                for a5 in soup.find_all('a',  class_='pic', href=True):
                                    if len(a5['class'] == 1):
                                        categories[index[i]][a2['title']
                                                             ][a3['title']][a4['title']][a5['title']] = {}
                                        URL = 'https://www.skroutz.gr' + \
                                            a5['href']
                                        page = requests.get(URL)
                                        soup = BeautifulSoup(
                                            page.content, 'html.parser')

                                        # e.g. manufacturer
                                        for div in soup.find_all('div', class_='filter-group'):
                                            if div.find('div') != None:
                                                if div.find('div').find('h3') != None:
                                                    if div.find('div').find('h3').find('button') != None:
                                                        categories[index[i]][a2['title']][a3['title']][a4['title']][a5['title']][div.find('div').find(
                                                            'h3').find('button').text] = {}

                                                        if div.find('ul') != None:
                                                            # e.g. nokia
                                                            for li in div.ul.find_all('li'):
                                                                if li.find('a') != None:
                                                                    categories[index[i]][a2['title']][a3['title']][a4['title']][a5['title']][div.find('div').find(
                                                                        'h3').find('button').text][li.find('a')['title']] = {}

                                # e.g. manufacturer
                                for div in soup.find_all('div', class_='filter-group'):
                                    if div.find('div') != None:
                                        if div.find('div').find('h3') != None:
                                            if div.find('div').find('h3').find('button') != None:
                                                categories[index[i]][a2['title']][a3['title']][a4['title']][div.find('div').find(
                                                    'h3').find('button').text] = {}

                                                if div.find('ul') != None:
                                                    # e.g. nokia
                                                    for li in div.ul.find_all('li'):
                                                        if li.find('a') != None:
                                                            categories[index[i]][a2['title']][a3['title']][a4['title']][div.find('div').find(
                                                                'h3').find('button').text][li.find('a')['title']] = {}

                        # e.g. manufacturer
                        for div in soup.find_all('div', class_='filter-group'):
                            if div.find('div') != None:
                                if div.find('div').find('h3') != None:
                                    if div.find('div').find('h3').find('button') != None:
                                        categories[index[i]][a2['title']][a3['title']][div.find('div').find(
                                            'h3').find('button').text] = {}

                                        if div.find('ul') != None:
                                            # e.g. nokia
                                            for li in div.ul.find_all('li'):
                                                if li.find('a') != None:
                                                    categories[index[i]][a2['title']][a3['title']][div.find('div').find(
                                                        'h3').find('button').text][li.find('a')['title']] = {}
        i += 1


with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(categories, fp, ensure_ascii=False, indent=4, sort_keys=True)
