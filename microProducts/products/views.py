from flask import Flask
from flask_cors import CORS

from products.controllers.product_controller import product_controller
from db.db import db
from flask_consulate import Consul

app = Flask(__name__)

CORS(app)

app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(product_controller)

# Registro de microservicio Productos
@app.route('/healthcheck')
def healthcheck():
    return 'OK', 200
    
consul = Consul(app=app)

consul.register_service(
    name='microProducts',
    interval='10s',
    tags=['products'],
    port=5003,
    httpcheck='http://192.168.80.3:5003/healthcheck'
)

if __name__ == '__main__':
    app.run()
