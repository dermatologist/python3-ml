import json
from PIL import Image
from io import BytesIO
import base64
import face_recognition as fr
import numpy as np
import cv2

# No warnings in production
import warnings

warnings.filterwarnings("ignore")


# Load model here
# model = 

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    result = {}
    try:
        event = json.loads(req)

        im = Image.open(BytesIO(base64.b64decode(event['img'])))
        im2 = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

        img_list = face_alignment(im2, scale=1.05)
        for img_aligned in img_list:
            retval, buffer = cv2.imencode('.jpg', img_aligned)
        result = {
            "function": "Aligned",
            "img": base64.b64encode(buffer).decode("utf-8")
        }
    except:
        result = {
            "function": "Error",
            "img": "Error"
        }

    return json.dumps(result)
