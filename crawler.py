import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import random


BOLD = '\033[1m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
GREEN = '\033[32m'
BLUE = '\033[34m'

def crawl_website(url, depth=1):
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
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
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

            print(url)

            crawled.add(url)
        
    #   if the site has rate limiting then remove the comment otherwise leave it as it is for faster results.
    #        time.sleep(random.uniform(1, 2))  


print('')
print('')
print(RESET + "-"*130)
target = input(BOLD + YELLOW + "Enter The Target You Want To Crawl: " + CYAN)
print(RESET + "-"*130)

print('')
print('')

print(BOLD + YELLOW + "Target: " + BOLD + CYAN + target + RESET)

print('')
print('')

print(BOLD + BLUE + """[+] Starting [+]
      
      """ + RESET + GREEN)

if not target.startswith('http'):
    target = 'https://' + target

crawl_website(target, depth=2)

print(BOLD + BLUE + """ 
      
[+] Finished [+]
      
      """)

