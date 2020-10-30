from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

json = requests.get("https://www.naver.com/srchrank?frm=main").json()

ranks = json.get("data")
#print(ranks)

for i in ranks:
    keyword=i.get("keyword")#span이 keyword인 것만을 get
    print(keyword)

#참고:https://code-nen.tistory.com/111