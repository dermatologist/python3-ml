import json
import os
import base64
from pathlib import PurePath

from fastai import *
from fastai.vision import *
from io import BytesIO

# No warnings in production
import warnings
warnings.filterwarnings("ignore")


FUNCTION_ROOT = os.environ.get("function_root", "/root/function")
MODEL_FILE = os.environ.get("model_file", "export.pkl")

learn = load_learner(FUNCTION_ROOT + '/model/', MODEL_FILE)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    event = json.loads(req)

    img = open_image(BytesIO(base64.b64decode(event['img'])))
    prediction = learn.predict(img)[0]
    return JSONResponse({'result': str(prediction)})

    result = {
        "function": "Function",
        "prediction": str(prediction)
    }


    return json.dumps(result)


