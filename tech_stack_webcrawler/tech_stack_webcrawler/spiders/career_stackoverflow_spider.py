import scrapy

class CareerStackoverflowSpider(scrapy.Spider):
    name = "careerstackoverflow"
    start_urls = [
        "http://careers.stackoverflow.com/companies"
    ]

    def parse(self, response):
        # print response.css(".list.companies").xpath("div").extract()
        filename = response.url.split("/")[-2] + ".html"
        with open(filename, "wb") as f:
            for sel in response.css(".list.companies").xpath("div"):
                f.write(sel.xpath("p/a[@class='title']/text()").extract()[0] + "\n")
