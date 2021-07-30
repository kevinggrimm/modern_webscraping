# modern_webscraping
udemy course - Modern Web Scraping with Python using Scrapy Splash Selenium

## Resource
### Sites
- [Try jsoup - Interactive HTML/XML Parser](#https://try.jsoup.org/)
- [XPath Playground - Interactive XPath Parser](#https://scrapinghub.github.io/xpath-playground/)
### StackOverflow
- [Running Scrapy on Lambda](#https://stackoverflow.com/questions/51349379/how-to-run-a-scrapy-spider-from-aws-lambda)
- [Get results from Scrapy on Lambda](#https://stackoverflow.com/questions/52291998/unable-to-get-results-from-scrapy-on-aws-lambda)
- [Scrapy in Lambda as a layer](#https://stackoverflow.com/questions/55022402/using-scrapy-in-aws-lambda-function-as-a-layer)
- [Package scrapy dependencies to Lambda](#https://stackoverflow.com/questions/57104229/how-to-package-scrapy-dependency-to-lambda)
- [](#)

## CSS Selectors
- *Note:* Using CSS Selectors when covering `Splash`
- Be careful with tag selection
- Don't want to just call tags by name
1. By class
`.className`
- Can belong to multiple elements
2. By id
`#idName`
- Belongs to single element
3. Multiple classes
- `.classOne.classTwo`
4. Attributes
- `elementName[identifierName=identifierValue]`

### Examples
1. 'a' elements where `href` starts with `https`
`a[href^='https']`
2. 'a' elements where `href` ends with `.fr`
`a[href$='fr']`
3. 'a' element where `href` contains `google`
`a[href*='google']`
4. All paragraphs inside a div with specific class
`div.intro p`
*Note:* `span` elements within the div are considered descendants and not included
- To add, change to `div.intro p, span`
5. All direct children of an element
`div.intro > p`
6. Elements immediately after an element
`div.intro + p`
7. First item in a list
`li:nth-child(1)`
8. First and third item
`li:nth-child(1), li:nth-child(3)`
9. Odd/even items in a list
`li:nth-child(odd)`
`li:nth-child(even)`

### Theory
1. Foreign Attributes
`[attributeName='value']
2. Value lookup
`[attributeName ^='start']`
`[attributeName ~='between']`
`[attributeName $='end']`
3. Position
4. Direct Children
- `Element > element`
#### CSS Combinators
1. All `p` elements place after the div
- There can be other elements inbetween
- `div ~ p`


## XPath Fundamentals
- Richer in functionality than CSS selectors
- Do not explicitly

### Examples
1. all h1 elements, regardless of position
`//h1`
2. `p` elements within `div` with specific class
`//div[@class='intro']/p`
3. `div` elements with class of `intro` or `outro`
- `or` logical operator
`//div[@class='intro' or @class='outro']/p`
4. Text value of selected elements
`//div[@class='intro' or @class='outro']/p/text()`
5. `href` value from link elements
`//a/@href`
6. Links where `href` starts with `https`
- `startwith()` function
`//a[start-with(@href, 'https')`
7. Links where `href` ends with `fr`
> **NOTE:** `ends-with` is only supported in XPath 2.0
- XML, Chrome only support 1.0 
`//a[ends-with(@href, 'fr')]`
8. Links where `href` has specific text
`//a[contains(@href, 'google')]`
9. Links where the *link text* (not href) contains specific text
- **NOTE:** Value passed is case sentitive
    - `text(), 'france'` vs `text(), France`
`//a[contains(text(), 'France')]`
10. First list item from an element
`//ul[@id='items']/li[1]`
11. First and last list elements
`ul//[@id='items']/li[position() = 1 or position() = last()]`
12. All list items after the first
`ul//[@id='items']/li[position() > 1]`

### XPath - Navigating Up The Tree
- Cannot do this with CSS Selectors
1. Parent of a `p` element where `p` id = `unique`
- Parent in XPath is called an **axis**
- Used to navigate the HTML marketup
`//p[@id='unique']/parent::div`
2. **NOTE:** Sometimes we do not know what the parent is 
`node()` - figures out the parent element
`//p[@id='unique']/parent::node()`
3. Ancestors - returns the parent and grandparent
`//p[@id='unique']/ancestor::node()`
4. Return ancestors or the element itself
`//p[@id='unique']/ancestor-or-self::node()`
5. *Preceding* - Returns all elements that precede the `p` element
- Excludes ancestors
`//p[@id='unique']/preceding`
**Example:** Get the `h1` element that precedes a `p`
`//p[@id='unique']/preceding::h1`
6. Preceding Sibling
- Brother element
- Elements are siblings if they share the same parent
`//p[@id='outside']/preceding-sibling::node()`

### XPath - Navigating Down The Tree
1. Get all `p` children of an element
`//div[@id='intro']/child::p`
2. Get all general children of an element
`//div[@id='intro']/child::node()`)
3. All elements that are listed after a specific `element`
- After the closing tag
`//div[@class='intro']/following::node()`
4. All elements after an element that share the same parent
`//div[@class='intro']/following-siblign::node()`
5. All children + grandchildren of an element
`//div[@class='intro']/descendant::node()`

### Xpath - Theory
1. Any element 
`//elementName`
2. Class name, ID or attribute
`elementName[@attribute='value']`
`elementName[@id='value']`
`elementName[@class='value']`
3. Position
`//li[1]`
`//li[position() = 1 or position() = 2]`
`//li[position() = 1 and contains(@text, 'hello')]`
4. Functions
`starts-with()`
`contains()`
`ends-with()` (*not supported for XPath 1.0*)
5. Predicates
- Conditions
- Content within `[]`
6. Axes
`axisName::elementName`
*Up:* 
- `parent`
- `ancestor`
- `preceding`
- `preceding-sibling`
*Down:*
- `child`
- `following` - elements after the closing tag of an element
- `following-sibling` - elements after the closing tag of an element
- `descendant` - children and grandchildren of element


## Scraping APIs
- `quotestoscrape.com/scroll`
- To check for APIs, go to *Network* tab, filter to *XHR* requests
- **XHR** stands for *XML and HTTP requests*
### Notes
- API URL will typically be different from website URL
- When scraping APIs, *always use the base template*
    - If you use a separate template, you cannot define the Rule object
    - Most of the time, there are no links to follow
- Flesh out the API structure before assembling scraper