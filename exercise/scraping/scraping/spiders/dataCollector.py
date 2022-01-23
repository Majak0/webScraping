import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        'https://www.tereva-direct.fr/A-538268-base-protection-chaussures-basses-k-road-b1000-noir-bleu',
    ]

    def parse(self, response):
        for product in response.css('div.product'):

            yield {
                'text': product.css('span.text::text').get(),
                'image': product.css('img.image').get()
            }