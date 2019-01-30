# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class MagicCorpSpider(scrapy.Spider):
    name = "Image and cards name"
    start_urls = ["http://www.magiccorporation.com/mc.php?rub=cartes&op=edition&num=225&mode=hybrid",]

    def parse(self, response):
        for card in response.xpath("//tr[@class='hover']"):
            name = card.xpath("string(td[4]/span/a/@title)").extract()
            image = card.xpath("td[1]/a/img/@src").extract()

            for item in zip(name,image):
                scraped_info = {
                'name' : item[0],
                'image' : item[1]
                }

                yield scraped_info
