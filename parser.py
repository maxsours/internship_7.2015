import requests
from bs4 import BeautifulSoup


def get_random_number_from_website(min=1, max=100):
    """
    get a random number from the html coming from the `random.org` website
    :param min: minimum integer range
    :param max: maximum interger range
    :return: the random integer that the website created
    """
    url = "https://www.random.org/integers/?num=1&min={min}&max={max}&col=1&base=10&format=html&rnd=new"

    r = requests.get(url.format(min=min, max=max))
    soup = BeautifulSoup(r.text, "html.parser")
    list_result = soup.pre.get_text().split()
    return [int(list_result[0]), r]
