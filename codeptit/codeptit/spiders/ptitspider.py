import scrapy
import json

class PtitspiderSpider(scrapy.Spider):
    name = "ptitspider"
    allowed_domains = ["code.ptit.edu.vn"]
    start_urls = ["https://code.ptit.edu.vn/student/question"]

    def start_requests(self):
        url = "https://code.ptit.edu.vn/student/question"
        cookie_location = "path/to/your/cookie.json"
        with open(cookie_location) as f:
            cookies = json.load(f)

        yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        table = response.css("table tr")
        for row in table[1:]:
            tds =row.css('td')
            yield {
                "stt": tds[1].css('::text').get(),
                "id": tds[2].css('a::text').get(),
                "title": tds[3].css('a::text').get(),
                "group": tds[4].css('::text').get(),
                "topic": tds[5].css('::text').get(),
                "difficulty": tds[6].css('::text').get(),
            }

        page_selection = response.css("ul.pagination li")
        next_page = page_selection[-1].css("a::attr(href)").get()

        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

