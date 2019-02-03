# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json

class MagicCorpSpider(scrapy.Spider):
    name = "Image and cards name"
    start_urls = ["http://www.magiccorporation.com/mc.php?rub=cartes&op=edition&num=225&mode=hybrid",]

    def parse(self, response):
        for card in response.xpath("//tr[@class='hover']"):
            nameVO = card.xpath("string(td[4]/span/a/@title)").extract()
            nameVF = card.xpath("string(td[5]/span/a/@title)").extract()
            image = card.xpath("td[1]/a/img/@src").extract()
            rarity = card.xpath("td[2]/img/@src").extract()
            color = card.xpath("td[6]/img[last()]/@src").extract()


            if(rarity == ['/images/magic/rarete/normal/mystic_rare.gif']):
                rarity = ["mythic"]
            elif(rarity == ['/images/magic/rarete/normal/uncommon.gif']):
                rarity = ["uncommon"]
            elif(rarity == ['/images/magic/rarete/normal/common.gif']):
                rarity = ["common"]
            elif(rarity == ['/images/magic/rarete/normal/rare.gif']):
                rarity = ['rare']

            if(color == ['/images/magic/manas/mini/w.gif']):
                color = ['white']
            elif(color == ['/images/magic/manas/mini/u.gif']):
                color = ['blue']
            elif(color == ['/images/magic/manas/mini/b.gif']):
                color = ['black']
            elif(color == ['/images/magic/manas/mini/r.gif']):
                color = ['red']
            elif(color == ['/images/magic/manas/mini/g.gif']):
                color = ['green']
            else:
                color = ['uncolor']

            for item in zip(nameVO, nameVF ,image, rarity, color):
                scraped_info = {
                'nameVO' : item[0],
                'nameVF' : item[1],
                'image' : item[2],
                'rarity' : item[3],
                'color' : item[4]
                }

                yield scraped_info
                with open('result.json', 'w') as fp:
                    json.dump(zip, fp)
