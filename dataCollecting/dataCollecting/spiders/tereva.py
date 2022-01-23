# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader


class TerevaSpider(scrapy.Spider):
    name = 'tereva'
    start_urls = ['https://www.tereva-direct.fr/A-538268-base-protection-chaussures-basses-k-road-b1000-noir-bleu']

    def parse(self, response):

        """
        Use the scrapy Pipelines to get the images and stock them in dataCollecting/dataCollecting/output

        for img in response.xpath("//img"):
            img_url = img.xpath("@src").extract_first()
            yield DatacollectingItem(file_urls=[img_url])

        -----------------------------------------------------

        Download all the pdf on the site and collect the data

        url = "https://www.tereva-direct.fr/A-538268-base-protection-chaussures-basses-k-road-b1000-noir-bleu"
        read = requests.get(url)
        html_content = read.content
        soup = BeautifulSoup(html_content, "html.parser")

        list_of_pdf = set()
        l = soup.find('.doc_technique')
        p = l.find_all('a')

        for link in (p):
            pdf_link = (link.get('href')[:-5]) + ".pdf"
            print(pdf_link)
            list_of_pdf.add(pdf_link)

        def info(pdf_path):
            response = requests.get(pdf_path)

            with io.BytesIO(response.content) as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()

            return information

        for i in list_of_pdf:
            info(i)
        """

        yield {
            'produit': response.css('h1::text').get(),
            'description': response.css('.toggle-wrap-container::text').getall(),
            'caracteristiques': response.css('.attribut::text, .value::text').getall(),
            'liens': response.css('.fa-download+span::text').getall()
        }