# -*- coding: utf-8 -*-
import scrapy
from admision.items import AdmisionItem

class AdmispiderSpider(scrapy.Spider):
    name = "admispider"
    allowed_domains = ["http://www.admision.uni.edu.pe/resultado_adm.php"]
    start_urls = (
        'http://www.admision.uni.edu.pe/resultado_adm.php/',
    )

    for i in range(1,272):
        i = str(i)
        start_urls = start_urls + ('http://www.admision.uni.edu.pe/resultado_adm.php?pagina=%s' %i, )

    def parse(self, response):

        alumnos= response.xpath('//tr[@class="lista_0"] | //tr[@class="lista_1"]')

        for alumno in alumnos:

            data = AdmisionItem()
            # datas =  response.xpath('//tr[@class="t_lista2"]/td/text()').extract()

            alumno = alumno.xpath('td')

            data['codigo'] = u''.join(alumno[1].xpath('text()').extract()).strip()
            data['nombre_completo'] = u''.join(alumno[2].xpath('text()').extract()).strip()
            data['P1'] = u''.join(alumno[3].xpath('text()').extract()).strip()
            data['P2'] = u''.join(alumno[4].xpath('text()').extract()).strip()
            data['P3'] = u''.join(alumno[5].xpath('text()').extract()).strip()
            data['acumulado'] = u''.join(alumno[6].xpath('text()').extract()).strip()
            data['nota_vocacional'] = u''.join(alumno[7].xpath('text()').extract()).strip()
            data['nota_cne'] = u''.join(alumno[8].xpath('text()').extract()).strip()
            data['nota_arq'] = u''.join(alumno[9].xpath('text()').extract()).strip()
            data['nota_final'] = u''.join(alumno[10].xpath('text()').extract()).strip()
            data['nota_ingreso'] = u''.join(alumno[11].xpath('text()').extract()).strip()
            data['merito_modalidad'] = u''.join(alumno[12].xpath('text()').extract()).strip()
            data['modalidad_ingreso'] = u''.join(alumno[13].xpath('text()').extract()).strip()
            data['especialidad_ingreso'] = u''.join(alumno[14].xpath('text()').extract()).strip()
            data['observacion'] = u''.join(alumno[15].xpath('text()').extract()).strip()

            yield data
