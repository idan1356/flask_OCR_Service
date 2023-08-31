from flask_restx import Namespace, Resource
from api.components.parsers import upload_parser
from api.components.data_models import response_model_template, error_model_template

from .utils.api_utils import process_image, validate_file_extension, validate_languages_selected
from .utils.misc import image_bytes_to_base64
from api.exceptions.exceptions import UnsupportedFileFormat, UnsupportedLanguageOfModel

ocr_ns = Namespace('api', description='Optical Character Recognition service')


@ocr_ns.errorhandler(UnsupportedFileFormat)
@ocr_ns.errorhandler(UnsupportedLanguageOfModel)
def handle_unsupported(error):
    return {'message': str(error)}, 400


@ocr_ns.route('/decipher-text')
class OCRImage(Resource):
    response_model = ocr_ns.model(*response_model_template)
    error_model = ocr_ns.model(*error_model_template)

    @ocr_ns.doc('upload-image-for-ocr', description='Upload an image for Optical Character Recognition',
                params={
                    'langs': 'Languages of text in image to be deciphered (see language list in config file)',
                    'get_processed_image': 'Whether the image processed by model be returned',
                })
    @ocr_ns.response(200, 'OCR successful', response_model)
    @ocr_ns.response(400, 'OCR unsuccessful', error_model)
    @ocr_ns.expect(upload_parser, validate=True)
    def post(self):
        # parse initial request
        parsed_request = upload_parser.parse_args()

        # get query params
        file_storage_image = parsed_request['user_image']
        languages_list = parsed_request['langs'].split(',')
        get_processed_image = parsed_request['get_processed_image']

        validate_file_extension(file_storage_image)
        validate_languages_selected(languages_list)

        # process image and create response
        ocr_reader_response, processed_image_byte_content = process_image(file_storage_image, languages_list)
        response = {"reader_data": ocr_reader_response}

        # add processed image if requested
        if get_processed_image:
            response["base64_processed_image_content"] = image_bytes_to_base64(processed_image_byte_content)

        return response, 200
