import os
from tornado import ioloop, web
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId

MONGODB_DB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME = 'orce'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class NamesHandler(web.RequestHandler):
    def get(self, codigo):
        print codigo
        results = db.resultados.find_one({"codigo": codigo})
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(list(results), default=json_util.default))
        print results


class GetNames(web.RequestHandler):
    def get(self):
        with open("nombres.txt") as names_file:
            names = json.load(names_file)
            self.set_header("Content-Type", "application/json")
            self.write(json.dumps(names, default=json_util.default))


class GetAccepted(web.RequestHandler):
    def get(self):
        with open("ingresantes.txt") as names_file:
            ingresantes = json.load(names_file)
            self.set_header("Content-Type", "application/json")
            self.write(json.dumps(ingresantes, default=json_util.default))

class ResultsHandler(web.RequestHandler):
    def get(self):
        pass


class StoriesHandler(web.RequestHandler):
    def get(self):
        stories = db.stories.find()
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(list(stories), default=json_util.default))

    def post(self):
        story_data = json.loads(self.request.body)
        story_id = db.stories.insert(story_data)
        print('story created with id ' + str(story_id))
        self.set_header("Content-Type", "application/json")
        self.set_status(201)

settings = {
    "template_path": os.path.join(os.path.dirname('__file__'), "templates"),
    "static_path": os.path.join(os.path.dirname('__file__'), "static"),
    "debug": True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/api/codigo/([^/]+)', NamesHandler),
    (r'/api/getNames', GetNames),
    (r'/api/getAccepted', GetAccepted),
    (r'/resultados', ResultsHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()
