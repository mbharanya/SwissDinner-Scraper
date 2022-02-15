import json
import os
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup
import datetime
from usp.tree import sitemap_tree_for_homepage
import locale
import argparse


def get_ld_json(url: str) -> dict:
    parser = "html.parser"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, parser)

    locale.setlocale(locale.LC_ALL, 'de_CH.utf8')

    air_time = soup.select(
        "div.article-detail__transmissions.article-detail__transmissions--item > time")[0].decode_contents()

    # Sa 26. Mai 2018 18.20 Uhr
    formatted_date = datetime.datetime.strptime(
        air_time[3:], '%d. %b %Y %H.%M Uhr')

    return (formatted_date.strftime('%Y-%m-%d'), json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents)))


def download(url):
    try:
        print(f"downloading {url}")
        (air_time, data) = get_ld_json(url)
        filename = f"Swissdinner-{air_time}-{data['headline'].strip()}".replace(":", ".") + ".mp4"
        command = f"youtube-dl -o /output/'{filename}' {data['video']['contentUrl']}"
        print(command)
        os.system(command)
    except Exception as e:
        print(e)

def fetch_sitemap(sitemap):
    sitemap_tree = sitemap_tree_for_homepage(sitemap)

    for page in sitemap_tree.all_pages():
        if page.url.startswith("https://tv.telezueri.ch/swissdinner"):
            download(page.url)


banner = """\033[0;31m
  _________       .__              ________  .__                            
 /   _____/_  _  _|__| ______ _____\\______ \\ |__| ____   ____   ___________ 
 \\_____  \\\\ \\/ \\/ /  |/  ___//  ___/|    |  \\|  |/    \\ /    \\_/ __ \\_  __ \\
 /        \\\\     /|  |\\___ \\ \\___ \\ |    `   \\  |   |  \\   |  \\  ___/|  | \\/
/_______  / \\/\\_/ |__/____  >____  >_______  /__|___|  /___|  /\\___  >__|   
        \\/                \\/     \\/        \\/        \\/     \\/     \\/       
        
\033[0m        Download SwissDinner Episodes
"""

parser = argparse.ArgumentParser(description=banner, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument(
    '--url', help='Direct url to crawl e.g. https://tv.telezueri.ch/swissdinner/heute-kocht-david-36-145058857')
parser.add_argument(
    '--sitemap', default="https://tv.telezueri.ch/sitemap.xml", help='Sitemap to crawl (default)')

args = parser.parse_args()
print(banner)

if(args.url):
    download(args.url)
elif (args.sitemap):
    fetch_sitemap(args.sitemap)
else:
    print("No url or sitemap specified")
