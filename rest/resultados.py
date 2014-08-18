# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pickle
import json
import io

client = MongoClient('localhost', 27017)
db = client.orce

resultados = db.resultados

with open("resultados.json") as json_file:
    resultadosJSON = json.load(json_file)
    print resultadosJSON[0]
    nombres = dict()
    ingresantes = []
    for result in resultadosJSON:
        # This is for the database
        post_id = resultados.insert(result)
        nombres[result['nombre_completo']] = str(post_id)
        if result['especialidad_ingreso'] == '':
            pass
        else:
            ingresantes.append(str(post_id))
    # print nombres

with io.open('nombres.txt', 'w', encoding='utf-8') as f:
    #I'm still having issues with scaping chracters like Mu\u0213213oz == Muñoz
    f.write(unicode(json.dumps(nombres)))
    # json.dump(nombres, f, sort_keys=True, indent=4)

with io.open('ingresantes.txt', 'w', encoding='utf-8') as f:
    f.write(unicode(json.dumps(ingresantes)))
