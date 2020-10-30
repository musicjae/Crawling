from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.daum.net/')
soup = BeautifulSoup(response, 'html.parser')
i=1 #순위추가
for anchor in soup.select("a.link_favorsch"):
    print(str(i)+'위: '+ anchor.get_text())
    i+=1