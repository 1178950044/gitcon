from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.baidu.com")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
for parent in soup.a.parents:
    if parent is None:
        print (parent)
    else:
        print (parent.name)

