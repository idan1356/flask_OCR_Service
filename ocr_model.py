import easyocr

from flask import current_app
from functools import lru_cache


class OCRModelSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.reader = easyocr.Reader(current_app.config["default_reader_language_setup"])

        return cls._instance


class LRUCachedOCRModel:
    @lru_cache(maxsize=5)
    def get_ocr_model(self, languages_set: frozenset) -> easyocr.Reader:
        return easyocr.Reader(list(languages_set))
