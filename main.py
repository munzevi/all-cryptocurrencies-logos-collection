import requests as re
import requests_random_user_agent
from bs4 import BeautifulSoup as bs
import wget

s = re.Session()

url = "" # redacted because of legal issues

page = re.get(url)
soup = bs(page.content,"html.parser")

table = soup.find("table#coin-list-wrapper")
imgs = soup.table.find_all('img',{"class":"lozad rounded"})

for count, string in enumerate(imgs):
    nac = string.next_sibling.next_sibling.string
    codes = nac[nac.find("(")+1:nac.find(")")]+".png"
    url = string['data-src']

    try:
        wget.download(url, out="images/"+codes)
    except:
        print(f'{count}. token {codes} could not downloaded!')
    else:
        print(f'{count}/{len(imgs)} downloaded: {codes}')
