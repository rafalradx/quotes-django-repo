import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

main_url = "https://quotes.toscrape.com"


@dataclass
class AuthorScraped:
    fullname: str
    born_date: str
    born_location: str
    description: str


def scrap_authors_links() -> dict[str:str]:
    authors_links = {}
    for page_num in range(1, 11):
        url = f"{main_url}/page/{page_num}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        authors = soup.find_all("small", class_="author")

        quotes = soup.find_all("div", class_="quote")
        for author, quote in zip(authors, quotes):
            author_name = author.text
            if author_name not in authors_links:
                authors_links[author_name] = quote.find("a")["href"]
    return authors_links


def scrap_author_details() -> list[AuthorScraped]:
    authors_details = []
    authors_data = scrap_authors_links()
    for author_name, link in authors_data.items():
        url = f"{main_url}{link}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        author = AuthorScraped(
            fullname=author_name,
            born_date=soup.find("span", class_="author-born-date").text,
            born_location=soup.find("span", class_="author-born-location").text,
            description=soup.find("div", class_="author-description").text.strip(),
        )
        authors_details.append(author)
    return authors_details
