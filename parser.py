import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=html&rnd=new")
soup = BeautifulSoup(r.text, "lxml")
list_result = soup.pre.get_text().split()
result = int(' '.join(list_result))
