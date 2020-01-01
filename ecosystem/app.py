import datetime
import os
import logging
import webbrowser
from flask import Flask
from flask_restplus import Resource, Api

# Set the logging output info
logname = "logs.txt"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

start_time = datetime.datetime.now()

app = Flask(__name__)
api = Api(app)

@api.route('/time')
class System(Resource):
    def get(self):
        return {'current_time': str(datetime.datetime.now())}

@api.route('/time_since_start')
class System(Resource):
    def get(self):
        return {'play_time': str(start_time - datetime.datetime.now())}

@api.route('/generate_customers')
class System(Resource):
    def get(self):
        return {"outcome" : "good game!"}

@api.route('/end_game')
class System(Resource):
    def get(self):
        os.system("sh end_game.sh")
        return {"outcome" : "good game!"}

if __name__ == '__main__':
    app.run(debug=True, port = 3000)
