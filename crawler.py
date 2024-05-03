import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import random
import warnings

# Suppress BeautifulSoup warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

BOLD = '\033[1m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RED = '\033[31m'

def crawl_website(url, depth=1, proxy=None):
    if depth < 0:
        return

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    crawled = set()
    to_crawl = [url]

    while to_crawl:
        url = to_crawl.pop(0)

        if url in crawled:
            continue

        try:
            if proxy:
                response = requests.get(url, proxies={"http": proxy, "https": proxy})
            else:
                response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(RED + str(e) + RESET)
            continue

        if response.status_code == 200:
            page_content = response.content
            soup = BeautifulSoup(page_content, 'html.parser')
            links = soup.find_all('a')

            for link in links:
                complete_url = urljoin(url, link.get('href'))
                complete_url_parsed = urlparse(complete_url)
                complete_url_domain = complete_url_parsed.netloc

                if complete_url_domain == domain:
                    to_crawl.append(complete_url)

            print(GREEN + url + RESET)

            crawled.add(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple website crawler.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="URL of the website to crawl.")
    group.add_argument("-l", "--list", help="Path to the file containing list of URLs to crawl.")
    parser.add_argument("--proxy", help="Proxy address to use for the requests.")
    args = parser.parse_args()

    if args.url:
        print(BOLD + YELLOW + "\n\nTarget: " + BOLD + CYAN + args.url + RESET)
        print(BOLD + BLUE + "\n\n[+] Starting [+]\n\n" + RESET + GREEN)
        if not args.url.startswith('http'):
            args.url = 'https://' + args.url
        crawl_website(args.url, depth=2, proxy=args.proxy)
    elif args.list:
        with open(args.list, 'r') as f:
            urls = f.read().splitlines()
            for url in urls:
                print(BOLD + YELLOW + "\n\nTarget: " + BOLD + CYAN + url + RESET)
                print(BOLD + BLUE + "\n\n[+] Starting [+]\n\n" + RESET + GREEN)
                if not url.startswith('http'):
                    url = 'https://' + url
                crawl_website(url, depth=2, proxy=args.proxy)
    print(BOLD + BLUE + "\n\n[+] Finished [+]\n\n" + RESET)
