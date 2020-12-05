import csv
import logging
import time
from os.path import exists

import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scrapper")


def get_quotes_info(data):
    all_quotes = []
    fieldnames = ['author', 'author_link', 'text']

    if data.ok:
        soup = BeautifulSoup(data.text, 'lxml')
        for quote in soup.select('div[class="quote"]'):
            text = quote.select_one('span.text').text.strip("“”")
            author = quote.select_one('small.author').text
            author_link = quote.select_one('small.author + a').get('href', )
            all_quotes.append({k: v for k, v in zip(fieldnames, [author, author_link, text])})
    return all_quotes, fieldnames


def get_author_info(data):
    authors = []
    fieldnames = ['name', 'born_date', 'born_location', 'author_description']

    if data.ok:
        soup = BeautifulSoup(data.text, 'lxml')
        name = soup.select_one('[class="author-title"]').text.strip()
        born_date = soup.select_one('[class="author-born-date"]').text.strip()
        born_location = soup.select_one('.author-born-location').text.strip()
        description = soup.select_one('.author-description').text.strip()
        authors.append(
            {k: v for k, v in zip(fieldnames, [name, born_date, born_location, description])}
        )
    return authors, fieldnames


def write_to_csv(fieldnames, path, data):
    add_fieldnames_row = not exists(path)
    with open(path, "a") as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        if add_fieldnames_row:
            writer.writeheader()
        for row in data:
            writer.writerow(row)


def get_all_quotes_from_pages(url):
    all_quotes, fieldnames = [], []
    page_url = f"{url}/page/1"
    next_page_url = True

    while next_page_url:
        logger.info(f" request to {page_url} started")
        data = requests.get(page_url)
        quotes, fieldnames = get_quotes_info(data)
        all_quotes += quotes

        soup = BeautifulSoup(data.text, 'lxml')
        next_page_url = (soup.select_one("ul.pager li.next a") or {}).get('href', '')
        page_url = url + next_page_url

        time.sleep(1)

    return all_quotes, fieldnames


def get_all_authors_info_from(links):
    all_authors_info, fieldnames = [], []
    for link in links:
        logger.info(f" request to {link} started")
        data = requests.get(link)

        authors, fieldnames = get_author_info(data)
        all_authors_info += authors

        time.sleep(1)

    return all_authors_info, fieldnames


if __name__ == '__main__':
    main_url = "http://quotes.toscrape.com"
    quotes_path = 'quotes.csv'
    authors_path = 'authors.csv'

    quotes_info, quotes_fieldnames = get_all_quotes_from_pages(main_url)
    write_to_csv(quotes_fieldnames, quotes_path, quotes_info)

    authors_links = {main_url + quote['author_link'] for quote in quotes_info}
    authors_info, author_fieldnames = get_all_authors_info_from(authors_links)
    write_to_csv(author_fieldnames, authors_path, authors_info)
