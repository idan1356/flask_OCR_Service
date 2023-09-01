from typing import List


class UnsupportedFileFormat(Exception):
    def __init__(self, user_file_extension_input, allowed_image_extensions):
        self.message = f"Unsupported image type: {user_file_extension_input}, Use supported types: {allowed_image_extensions}"
        super().__init__(self.message)


class UnsupportedLanguageOfModel(Exception):
    def __init__(self, user_language_input: List):
        self.message = f"One or more of the following languages is not supported: {user_language_input}," \
                       f"see config file for supported langs by model."
        super().__init__(self.message)


def handle_unsupported(error):
    return {'message': str(error)}, 400