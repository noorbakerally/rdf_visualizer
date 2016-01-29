from flask import Flask
app = Flask(__name__)

#registering blueprints for apiv1
from appv1.loader import loader
app.register_blueprint(loader,url_prefix="/v1/loader")

if __name__ == "__main__":
        app.debug = True
        app.run()
