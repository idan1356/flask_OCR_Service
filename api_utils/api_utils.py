from flask import current_app
from werkzeug.datastructures import FileStorage

from ocr_utils.OCR_model import OCRModelSingleton
from api_utils.misc import get_file_extension_from_name, add_sentence_outline_to_image


def validate_file_extension(user_image_file: FileStorage):
    file_extension = get_file_extension_from_name(user_image_file.filename)
    allowed_image_formats = current_app.config["allowed_image_formats"]

    if file_extension.upper() not in allowed_image_formats:
        raise ValueError(f"Unsupported image type: {file_extension},"
                         f"Use supported types: {allowed_image_formats}")


def process_image(user_file_image: FileStorage) -> tuple:
    image_byte_content = user_file_image.read()
    file_extension = get_file_extension_from_name(user_file_image.filename)

    ocr_reader_response = OCRModelSingleton().reader.readtext(image_byte_content)
    sentence_outline_rectangles = [entry[0] for entry in ocr_reader_response]
    image_byte_content = add_sentence_outline_to_image(image_byte_content, sentence_outline_rectangles, file_extension)

    return ocr_reader_response, image_byte_content
