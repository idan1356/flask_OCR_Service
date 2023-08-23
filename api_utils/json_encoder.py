import json
import numpy as np


class NumpyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.float64):
            return float(obj)
        if isinstance(obj, np.int32):
            return int(obj)
        return json.JSONEncoder.default(self, obj)