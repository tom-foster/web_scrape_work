## Scrape the main website, webpage
## Once the webpages have been scrapped then analyse the pages
## For reading levels?
## TF 19/08/19
import scrapy
import re

class WarwickshireSpider(scrapy.Spider):
    # the cli argument
    name = 'wcc'
    start_urls = [
        'https://warwickshire.gov.uk',
    ]

    # extend the class
    def __init__(self):
        super(scrapy.Spider, self).__init__()
        self.pattern = re.compile('^https://www.warwickshire.gov.uk')
        self.visited_pages = []
        # not yet implemented
        self.visited_pages_all_links = {}

    def parse(self, response):
        for weblink in response.css("a:attr(href)").getall():
            yield {
                'weblink' : weblink,
            }
            ## write out pages_all links
            ## TODO
            if self.pattern.search(weblink):
                yield scrapy.Request(response.urljoin(weblink), callback=self.parse)
                page = response.url
                if page not in self.visted_pages:
                    self.visited_pages.append(page)
                filename = 'visited_pages_only_wcc.txt'
                with open(filename, 'w') as f:
                    for x in range(len(self.visited_pages)):
                        f.write(self.visited_pages[x] + '\n')