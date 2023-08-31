import easyocr

from flask import current_app
from functools import lru_cache


class LRUCachedOCRModel:
    @lru_cache(maxsize=5)
    def get_ocr_model(self, languages_set: frozenset) -> easyocr.Reader:
        return easyocr.Reader(list(languages_set))
