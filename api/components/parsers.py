from flask_restx import reqparse, inputs
from werkzeug.datastructures import FileStorage

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('user_image', location='files', type=FileStorage, required=True,
                           help='Image file to be deciphered by model (JPEG, GIF, PNG)')
upload_parser.add_argument('langs', default='en', type=str, location='args')
upload_parser.add_argument('get_processed_image', default=False, type=inputs.boolean, location='args')
