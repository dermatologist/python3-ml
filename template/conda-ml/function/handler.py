import json
import os
# No warnings in production
import warnings

warnings.filterwarnings("ignore")

# function_root = os.environ.get("function_root")
# Load model here
# model =


def handle(req: bytes) -> str:
    """handle a request to the function
    Args:
        req (bytes): request body
    """

    try:
        pass
    except:
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'html', 'upload.html')

        with (open(path, 'r')) as file:
            html = file.read()

        return html
