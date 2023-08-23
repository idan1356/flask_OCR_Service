import json

from flask import Flask, render_template
from flask_restx import Api

from api import ocr_ns
from api_utils.json_encoder import NumpyJSONEncoder

# app settings
app = Flask(__name__)
app.config["RESTX_JSON"] = {"cls": NumpyJSONEncoder}


# add custom config
with open('config.json') as config_file:
    config = json.load(config_file)
    app.config.update(config)


@app.route('/')
def index_page():
    return render_template("index_page.html")


api = Api(app, version='1.0', title='OCR service', description='OCR', doc='/api/docs')
api.add_namespace(ocr_ns)


if __name__ == "__main__":
    app.run(debug=False)
