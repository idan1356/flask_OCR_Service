from functools import lru_cache

import easyocr
from flask import current_app


class OCRModelSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.reader = easyocr.Reader(current_app.config["default_reader_language_setup"])

        return cls._instance


class CachedOCRModel:
    def __init__(self):
        self.models = {}

    @lru_cache(maxsize=5)
    def get_ocr_model(self, languages_set: frozenset) -> easyocr.Reader:
        if languages_set not in self.models:
            ocr_model = easyocr.Reader(list(languages_set))
            self.models[languages_set] = ocr_model

        return self.models[languages_set]
