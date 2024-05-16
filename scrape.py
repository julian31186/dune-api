import requests
import json
import math
from bs4 import BeautifulSoup

trail = '/wiki/Special:AllPages'
base = 'https://dune.fandom.com'
response = requests.get(base + trail)
soup = BeautifulSoup(response.content, 'html.parser')
page_cnt = 0
data = {}
cnt = 0
throttle = math.inf

#Clear files before scraping
with open('./README.txt', 'w') as f:
    f.write('All Pages API Provides\n\n')

with open('./data.json', 'w') as f:
    f.write('')

def is_content(soup):
    return (
        soup.find('a', string=lambda text: text and 'Next page' in text) is not None 
        or
        soup.find('a', string=lambda text: text and 'Previous page' in text) is not None 
    )

def handle_page(page, link):
    stripped_page = "_".join((page.strip().lower()).replace("/","_").replace("\"","").replace("\'","").replace(".","").replace(",","").replace("(","").replace(")","").split(" "))
    desc = ""
    
    res = requests.get(base + link)
    s = BeautifulSoup(res.content, 'html.parser')
    target_dev = s.find('div', class_='mw-parser-output')

    if target_dev:
        for p in target_dev.find_all('p'):
            txt = p.text.encode('ascii', 'ignore').decode()
            txt = txt.strip()

            desc += txt

        if len(desc) > 0:

            with open('./README.txt', 'a') as f:
                f.write(stripped_page + '\n')

            data[stripped_page] = {
                "description" : f'{desc}',
                "wiki" : f'{base}{link}',
            }

while is_content(soup) and cnt < throttle:

    target_div = soup.find('div', class_='mw-allpages-body')

    if target_div:
        for li in target_div.find_all('li'):
            handle_page(li.text, li.find('a')['href'])
            
        page_cnt += 1
        print(f'Handled Page -> {page_cnt}')
            
    next_page = soup.find('a', string=lambda text: text and 'Next page' in text)
    if next_page:
        response = requests.get(base + next_page['href'])
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        break

    cnt += 1

with open('./data.json', 'w') as f:
    f.write(json.dumps(data, indent=4))

print("Done!")
print(f'Pages -> {page_cnt}')