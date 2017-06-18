# Simple Spider for Powershell articles from 'Hey! Scripting Guy'
Dead-simple web crawler to scrape powershell articles from Microsoft technet blog [Hey! Scripting Guy](https://blogs.technet.microsoft.com/heyscriptingguy/)
The results are stored in a simple csv file.

## How to Run
First, be sure you have `lxml` python package installed
Install dependencies for this project using `pip`
```
pip install -r requirements.txt
```

This project is based on `scrapy` framework, so to run it you have two ways
either
```
$scrapy crawl pstip
```
or
```
python quickstart.py
```
The above are doing the same thing of kicking off the spider.