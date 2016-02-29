import scrapy

class CareerStackoverflowSpider(scrapy.Spider):
    name = "careerstackoverflow"
    start_urls = [
        "http://careers.stackoverflow.com/companies"
    ]

    # Notice that the path to the targeted data might change in the future.
    def parse(self, response):
        for company_link in response.css(".list.companies").xpath("div/div[@class='text']/p/a[@class='title']/@href"):
            if company_link:
                company_link = response.urljoin(company_link.extract())
                yield scrapy.Request(company_link, self.parse_company)

    def parse_company(self, response):
        file = open("tech.json", "a")
        tech_stack = response.xpath("//div[@data-company-section='tech-stack']/div[@class='tags']")

        if tech_stack:
            for tech_tag in tech_stack.xpath("a[contains(@class, 'post-tag')]/text()"):
                file.write(tech_tag.extract() + "\n")

        file.close()
