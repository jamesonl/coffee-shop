from game_config import gameConfig
import logging
import webbrowser
from flask import Flask
from flask_restplus import Resource, Api

settings = gameConfig(logging = False, starting_budget = 5000, \
                      player_name = "Jameson", player_email = "jameson@email.com")

# Set the logging output info
if settings.logging == False:
    subprocess.Popen("")
    logname = "logs/logs.txt"
    logging.basicConfig(filename=logname,
                                filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
    logging.info("Instantiated fiveharbors in **Test** Mode.")
else:
    logname = "logs.txt"
    logging.basicConfig(filename=logname,
                                filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
    logging.info("Instantiated fiveharbors in **Production** Mode.")

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
