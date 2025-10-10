import scrapy
import re
from datetime import datetime

class SiteSpider(scrapy.Spider):
    name = 'giliard'
    allowed_domains = ['giliardgodoi.github.io']
    start_urls = [
        'https://giliardgodoi.github.io/'
    ]
    visited = set()

    # pattern_link_to_file = re.compile(r"[.pdf|.jpeg|.jpg|.png|.gif|.doc|.docx|.xls|.xlsx|.ppt|.pptx]$")

    def parse(self, response):
        links = response.xpath('//a[not(starts-with(@href, "#"))]/@href')

        base = {
            'url' : response.url,
            'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status' : response.status
        }

        for link in links:
            url = response.urljoin(link.extract())
            print(type(url))
            if url not in self.visited:
                self.visited.add(url)
                yield scrapy.Request(url, self.parse)
                yield {**base, 'link' : url}

class SiteCamara(SiteSpider):
    name = 'camara'
    allowed_domains = ['santoantoniodaplatina.pr.leg.br']
    start_urls = [
        'https://www.santoantoniodaplatina.pr.leg.br/'
    ]
    visited = set()