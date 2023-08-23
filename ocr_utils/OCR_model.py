from flask import current_app
import easyocr

from functools import lru_cache
from typing import List


class OCRModelSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.reader = easyocr.Reader(current_app.config["default_reader_language_setup"])

        return cls._instance


class DynamicOCRModel:
    def __init__(self):
        self.models = {}

    @lru_cache(maxsize=5)
    def get_ocr_model(self, languages: List) -> easyocr.Reader:
        model_key = frozenset(languages)
        if model_key not in self.models:
            ocr_model = easyocr.Reader(languages)
            self.models[model_key] = ocr_model

        return self.models[model_key]
