import requests
from bs4 import BeautifulSoup

FORM_LINK = "https://forms.gle/D3v9AkgS9kFYjYGS8"
OLX_LINK = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/gdansk/?search%5Bfilter_enum_rooms%5D%5B0%5D=three"


def get_olx_data():
    """fetches data from one olx page, 44 oferts info"""
    page = requests.get(url=OLX_LINK)
    soup = BeautifulSoup(page.text, "html.parser")
    offerts = soup.select(".offer-wrapper")

    links = []
    prices = []
    addresses = []
    for offert in offerts:
        links.append(offert.select_one("tr .photo-cell a").get("href"))
        prices.append(offert.select_one(".price strong").getText())
        addresses.append(offert.select_one(".bottom-cell div p .breadcrumb span").getText())

    return links, prices, addresses

