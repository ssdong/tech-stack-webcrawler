import scrapy

class CareerStackoverflowSpider(scrapy.Spider):
    name = "careerstackoverflow"
    start_urls = [
        "http://careers.stackoverflow.com/companies"
    ]

    def parse(self, response):
        for company_link in response.css(".list.companies").xpath("div/p/a[@class='title']/@href"):
            if company_link:
                company_link = response.urljoin(company_link.extract())
                yield scrapy.Request(company_link, self.parse_company)

    def parse_company(self, response):
        tech_stack = response.xpath("//div[@data-company-section='tech-stack']")

        if tech_stack:
            for tech_tag in tech_stack.xpath("div[@class='tags']/span[@class='post-tag']/text()"):
                print tech_tag.extract()
