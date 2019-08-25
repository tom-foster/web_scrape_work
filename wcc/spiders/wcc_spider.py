## Scrape the main website, webpage
## Once the webpages have been scrapped then analyse the pages
## For reading levels?
## TF 19/08/19
import scrapy
import re

class WarwickshireSpider(scrapy.Spider):
    # the cli argument
    name = 'warks'
    start_urls = [
        'https://warwickshire.gov.uk',
    ]

    # extend the class
    def __init__(self):
        super().__init__()
        self.pattern = re.compile('^(https://|http://|https://www.|http://www.)warwickshire.gov.uk')
        self.visited_pages = []
        # not yet implemented
        self.visited_pages_all_links = {}
        self.count = 0

    def parse(self, response):
        page = response.url
        if page not in self.visited_pages_all_links.keys():
            self.visited_pages_all_links[page] = response.css('a::attr(href)').getall()
        filename = 'visited_pages_all_links.txt'
        with open(filename, 'w') as f:
            for k, v in self.visited_pages_all_links.items():
                f.write(k + '\n')
                for x in range(len(v)):
                    f.write('\t' + v[x] + '\n')
            
        for weblink in response.css("a::attr(href)").getall():
            yield {
                'weblink' : weblink,
            }
            ## write out pages_all links
            ## TODO
            if self.pattern.search(weblink):
                yield scrapy.Request(response.urljoin(weblink), callback=self.parse)
                if page not in self.visited_pages:
                    self.visited_pages.append(page)
                filename = 'visited_pages_only_wcc.txt'
                with open(filename, 'w') as f:
                    for x in range(len(self.visited_pages)):
                        f.write(self.visited_pages[x] + '\n')

        ## We want to parse all the pages that then get pushed to the 
