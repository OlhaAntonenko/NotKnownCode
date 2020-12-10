import csv
import logging
import re
import time
from os.path import exists

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger("scrapper")


def get_phone_and_name_url_by_ad_url(session, url):
    logger.info(f"request to ad {url}")
    ad_data = session.get(url)
    soup = BeautifulSoup(ad_data.text, 'lxml')
    time.sleep(1)

    get_phone_token = "var phoneToken = '(.+?)';"
    get_id = "'id':'(.+?)'"
    phone_token = re.findall(get_phone_token, ad_data.text)
    id_ = re.findall(get_id, ad_data.text)
    phone_url = f"https://www.olx.ua/ajax/misc/contact/phone/{id_[0]}/?pt={phone_token[0]}"

    logger.info(f"request to phone url {phone_url}")
    phone = session.get(phone_url)
    name = soup.select_one("div.offer-user__actions a").text.strip()
    time.sleep(1)

    return name, phone.json()['value']


def get_ads_url_by_category_url(url):
    logger.info(f"request to category {url}")  # one category
    category_data = requests.get(url)
    category_soup = BeautifulSoup(category_data.text, 'lxml')
    ads_data = category_soup.select("a[class='marginright5 link linkWithHash detailsLink']")
    return [re.findall(r'(.+\.html)', i.get('href', ''))[0] for i in ads_data]


def get_categories_url_by_region_url(url):
    logger.info(f"request to region url {url}")
    region_data = requests.get(url)
    region_soup = BeautifulSoup(region_data.text, 'lxml')
    return [re.sub("\s+", "", i.text) for i in region_soup.select("loc")]


def get_regions_url_by_sitemap(sitemap_url):
    logger.info(f"request to sitemap url {sitemap_url}")
    data = requests.get(main_url)
    soup = BeautifulSoup(data.text, 'lxml')
    return [i.text.strip() for i in soup.select("loc")]


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
    main_url = "https://www.olx.ua/sitemap.xml"
    users_data_path = 'users_data.csv'
    users_data_fieldnames = ['name', 'phone']
    users_data = []

    first_region_url = get_regions_url_by_sitemap(main_url)[0]
    time.sleep(1)

    categories_url = get_categories_url_by_region_url(first_region_url)
    time.sleep(1)

    one_category = categories_url[1]
    ads_links = get_ads_url_by_category_url(one_category)
    time.sleep(1)

    for ad_link in ads_links[:5]:  # first five ads
        session.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.66 Safari/537.36",
            "referer": ad_link
        }

        name_and_phone = get_phone_and_name_url_by_ad_url(session, ad_link)
        users_data.append({k: v for k, v in zip(users_data_fieldnames, name_and_phone)})

    write_to_csv(users_data_fieldnames, users_data_path, users_data)
