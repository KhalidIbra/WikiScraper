import requests
from bs4 import BeautifulSoup
import random

# This endless scraper program will extract the title from the specified wiki article and
# find a random link within it before extracting the title from that link and repeating the process
# Thus creating an endless scraper

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])


scrapeWikiArticle("https://en.wikipedia.org/wiki/Didier Drogba")

