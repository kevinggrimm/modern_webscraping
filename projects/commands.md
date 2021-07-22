## Scrapy Commands

```bash
# start a project
scrapy startproject worldometers

# generate a spider
# by default, scrapy (a) uses HTTPS protocol (b) adds final "/"
scrapy genspider countries www.worldometers.info/world-population/population-by-country
```

### Scrapy Shell
- Use before building spider
- Debug XPath expressions
**Shortcuts:** Use these most of the time
```bash
scrapy shell

# fetch URL
fetch("https://www.worldometers.info/world-population/population-by-country/")

# construct request object
r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")
fetch(r)

# output HTMl markup
response.body

# get title
title = response.xpath("//h1")

# get title text
title = response.xpath(\"//h1/text()\")

# get all countries
countries = response.xpath("//td/a/text()").getall()
```

### Execute a Spider
```bash
# from the root folder of the project (same level as scrapy.cfg)
scrapy crawl countries

```

### Section 4 - Spiders
```bash

```