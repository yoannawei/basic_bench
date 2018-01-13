import tornado.ioloop
import tornado.web
import json
from datetime import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({
            "current UTC" : datetime.utcnow().strftime('%Y-%m-%d'),
            "IP address" : self.request.remote_ip
        }))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()
    print(ioloop.time())
    ioloop.close()