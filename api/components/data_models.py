from flask_restx import fields

response_model_template = 'Successful Response', {
    'reader_data': fields.Arbitrary,
    'base64_processed_image_content': fields.String(example="base64 string content of processed image bytes", optional=True)
}

error_model_template = 'Unsuccessful Response', {
    'message': fields.String(example="error message")
}