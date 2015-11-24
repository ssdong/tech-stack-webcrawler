import scrapy

class CareerStackoverflowSpider(scrapy.Spider):
    name = "careerstackoverflow"
    start_urls = [
        "http://careers.stackoverflow.com/companies?pg=4"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + ".html"
        # with open(filename, "wb") as f:
        #     f.write(response.body)

        for company_link in response.css(".list.companies").xpath("div/p/a[@class='title']/@href"):
            if company_link:
                company_link = response.urljoin(company_link.extract())
                yield scrapy.Request(company_link, self.parse_company)

    def parse_company(self, response):
        print "This is a test"
