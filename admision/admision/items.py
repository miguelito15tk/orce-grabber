# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AdmisionItem(scrapy.Item):
    codigo = scrapy.Field()
    nombre_completo = scrapy.Field()
    P1 = scrapy.Field()
    P2 = scrapy.Field()
    P3 = scrapy.Field()
    acumulado = scrapy.Field()
    nota_vocacional = scrapy.Field()
    nota_examen = scrapy.Field()
    nota_final = scrapy.Field()
    modalidad_ingreso = scrapy.Field()
    especialidad_ingreso = scrapy.Field()
    observacion= scrapy.Field()
