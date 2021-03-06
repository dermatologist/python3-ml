import json
import os
# from pathlib import PurePath
import base64
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

    if req is empty try will fail and the except will display image upload page.
    Upload page submits to the function.
    """
    try:

        event = json.loads(req)

        img = open_image(BytesIO(base64.b64decode(event['img'])))
        prediction = learn.predict(img)[0]

        result = {
            "function": "Function",
            "prediction": str(prediction)
        }
        return json.dumps(result)

    except:
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'html', 'upload.html')

        with(open(path, 'r')) as file:
            html = file.read()

        return html
