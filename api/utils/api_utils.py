from flask import current_app
from typing import List
from werkzeug.datastructures import FileStorage

from ocr_model import CachedOCRModel
from api.utils.misc import get_file_extension_from_name, add_sentence_outline_to_image


def validate_file_extension(user_image_file: FileStorage)-> None:
    file_extension = get_file_extension_from_name(user_image_file.filename)
    allowed_image_formats = current_app.config["allowed_image_formats"]

    if file_extension.upper() not in allowed_image_formats:
        raise ValueError(f"Unsupported image type: {file_extension},"
                         f"Use supported types: {allowed_image_formats}")


def validate_languages_selected(user_languages_list: List) -> None:
    # check if user languages list is subset of list of languages supported by model
    if not all(lang in current_app.config["supported_languages"] for lang in user_languages_list):
        raise ValueError(f"One or more of the following languages is not supported: {user_languages_list},"
                         f"see config file for supported langs by model.")


def process_image(user_file_image: FileStorage, languages_list: List) -> tuple:
    image_byte_content = user_file_image.read()
    file_extension = get_file_extension_from_name(user_file_image.filename)

    ocr_reader_response = CachedOCRModel().get_ocr_model(frozenset(languages_list)).readtext(image_byte_content)
    sentence_outline_rectangles = [entry[0] for entry in ocr_reader_response]
    image_byte_content = add_sentence_outline_to_image(image_byte_content, sentence_outline_rectangles, file_extension)

    return ocr_reader_response, image_byte_content
