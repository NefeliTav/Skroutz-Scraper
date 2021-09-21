from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time

index = ['Τεχνολογία', 'Σπίτι-Κήπος', 'Μόδα', 'Hobby-Αθλητισμός',
         'Υγεία-Ομορφιά', 'Παιδικά-Βρεφικά', 'Auto - Moto', 'Επαγγελματικά - B2B']

categories = {}
categories['Τεχνολογία'] = {}
categories['Σπίτι-Κήπος'] = {}
categories['Μόδα'] = {}
categories['Hobby-Αθλητισμός'] = {}
categories['Υγεία-Ομορφιά'] = {}
categories['Παιδικά-Βρεφικά'] = {}
categories['Auto - Moto'] = {}
categories['Επαγγελματικά - B2B'] = {}
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.skroutz.gr/')
html = driver.page_source
'''


options = Options()
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(options=options)


driver.get('https://www.skroutz.gr/')
html = driver.page_source
driver.quit()

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
        time.sleep(0.5)

        for a2 in soup.find_all('a', class_='pic', href=True):  # e.g. mobile
            if len(a2['class']) == 1:
                categories[index[i]][a2['title']] = {}
                URL = 'https://www.skroutz.gr/' + a2['href']
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                time.sleep(0.5)

                # e.g. mobile phones
                for a3 in soup.find_all('a', class_='pic', href=True):
                    if len(a2['class']) == 1:
                        categories[index[i]][a2['title']][a3['title']] = {}
                        URL = 'https://www.skroutz.gr' + a3['href']
                        page = requests.get(URL)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        time.sleep(0.5)

                        for a4 in soup.find_all('a',  class_='pic', href=True):
                            if len(a4['class']) == 1:
                                categories[index[i]][a2['title']
                                                     ][a3['title']][a4['title']] = {}
                                URL = 'https://www.skroutz.gr' + a4['href']
                                page = requests.get(URL)
                                soup = BeautifulSoup(
                                    page.content, 'html.parser')
                                time.sleep(0.5)

                                for a5 in soup.find_all('a',  class_='pic', href=True):
                                    time.sleep(0.5)
                                    if len(a5['class']) == 1:
                                        categories[index[i]][a2['title']
                                                             ][a3['title']][a4['title']][a5['title']] = {}
                                        URL = 'https://www.skroutz.gr' + \
                                            a5['href']
                                        page = requests.get(URL)
                                        soup = BeautifulSoup(
                                            page.content, 'html.parser')

                                        # e.g. manufacturer
                                        for div in soup.find_all('div', class_='filter-group'):
                                            time.sleep(0.5)
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
                                    time.sleep(0.5)
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
                            time.sleep(0.5)
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
    json.dump(categories, fp, ensure_ascii=False, indent=6, sort_keys=True)
