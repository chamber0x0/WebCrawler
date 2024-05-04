
# Python Web Crawler

This repository contains a simple and effective web crawler written in Python. It navigates webpages within a domain, avoiding duplicate URLs, and provides colored terminal output. Ideal for website testing and security research.

## Features

- Navigates webpages within a given domain
- Avoids duplicates
- Provides formatted output for btter readability
- Supports crawling multiple domains from a list
- Supports using a proxy for the requests

## Usage

1. Clone this repository
``` 

git clone https://github.com/chamber0x0/WebCrawler.git 

```
2. Navigate to the directory
```

cd WebCrawler

```
3. Give necessary permissions if needed
```

chmod +x crawler.py

```
4. Run the script with Python 3. You can use the `-u` flag for a single URL, the `-l` flag for a list of URLs, and the `--proxy` flag to specify a proxy.
```
python3 crawler.py -h
python3 crawler.py -u https://example.com
python3 crawler.py -l domains.txt     # Path to the file that conatains list of domains.
python3 crawler.py -u https://example.com --proxy http://127.0.0.1:8080   # This is jsut example proxy use the one which your proxy tool is configured to.

```

## Note 

If the site has rate limiting you can uncomment this line `time.sleep(random.uniform(1, 2))` in the script to avoid any IP blocks.

![image](https://github.com/chamber0x0/WebCrawler/assets/160602770/c308b749-5963-4322-abe2-b919c9d170f8)

## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library

