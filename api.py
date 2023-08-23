from flask_restx import Namespace, Resource, reqparse
from werkzeug.datastructures import FileStorage

from api_utils.api_utils import process_image, validate_file_extension
from api_utils.misc import image_bytes_to_base64

ocr_ns = Namespace('api', description='Optical Character Recognition service')


@ocr_ns.route('/decipher-text')
class OCRImage(Resource):
    upload_parser = reqparse.RequestParser()
    upload_parser.add_argument('user_image', location='files', type=FileStorage,
                               required=True, help='Image file (JPG, JPEG, PNG)')

    @ocr_ns.doc('upload-image-for-ocr', description='Upload an image for Optical Character Recognition')
    @ocr_ns.expect(upload_parser, validate=True)
    def post(self):
        file_storage_image = self.upload_parser.parse_args()['user_image']
        response = {}

        try:
            validate_file_extension(file_storage_image)
        except ValueError as e:
            return {"message:": str(e)}

        ocr_reader_response, processed_image_byte_content = process_image(file_storage_image)
        response["reader_data"] = ocr_reader_response
        response["base64_processed_image_content"] = image_bytes_to_base64(processed_image_byte_content)
        return response, 200
