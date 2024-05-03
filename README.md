# Python Web Crawler

This repository contains a simple and effective web crawler written in Python. It navigates webpages within a domain, avoiding duplicate URLs, and provides colored terminal output. Ideal for website testing and security research.

## Features

- Navigates webpages within a given domain
- Avoids crawling the same URL twice
- Provides colored terminal output

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
4. Run the script with Python 3
```

python3 crawler.py

```


## Note 

if the site has rate limiting you can uncomment this line `time.sleep(random.uniform(1, 2))` in the script to avoid any IP blocks.

![image](https://github.com/chamber0x0/WebCrawler/assets/160602770/c308b749-5963-4322-abe2-b919c9d170f8)



## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library


