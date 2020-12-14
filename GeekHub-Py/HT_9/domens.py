import csv
import logging
import random
import time
from os.path import exists

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger("scrapper")


def write_to_csv(fieldnames, path, data):
    add_fieldnames_row = not exists(path)
    with open(path, "a") as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        if add_fieldnames_row:
            writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    session = requests.session()
    main_url = "https://www.expireddomains.net"
    domains_path = 'domains.csv'
    domains = []

    page_url = "/deleted-domains/?&ftlds[]=8"
    session.headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.66 Safari/537.36",
        "Remote Address": "116.202.172.96:443",
        "Referrer Policy": "same - origin",
        "referer": main_url + page_url
    }

    fields = ['domain', 'bl', 'domainpop', 'abirth', 'aentries', 'alexa', 'dmoz',
              'statuscom', 'statusnet', 'statusorg', 'statusde',
              'statustld_registered', 'related_cnobi', 'changes', 'whois']

    while page_url:
        url = main_url + page_url
        session.headers.update({"referer": url})
        logger.info(f"request to filter url {url}")
        response = session.get(url)

        soup = BeautifulSoup(response.text, 'lxml')
        all_rows = soup.select('tbody tr')
        logger.info(f"received {len(all_rows)} domains")

        for r in all_rows:
            col_soup = BeautifulSoup(str(r), 'lxml')

            csv_row = {}
            for field in fields:
                select_obj = col_soup.select_one(f'td.field_{field}')
                csv_row[field] = (select_obj.a or select_obj).text

            domains.append(csv_row)

        next_button = soup.select_one('a.next')
        page_url = next_button.get('href') if next_button else None
        time.sleep(random.randint(1, 3))

    write_to_csv(fields, domains_path, domains)
