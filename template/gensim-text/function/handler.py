import json
import os
from gensim.models import KeyedVectors
from .utils import similar

# No warnings in production
import warnings
warnings.filterwarnings("ignore")


FUNCTION_ROOT = os.environ.get("function_root", "/root/function")
MODEL_FILE = os.environ.get("model_file", "export.bin")

# Load model here
model = KeyedVectors.load_word2vec_format(FUNCTION_ROOT + '/model/' + MODEL_FILE, unicode_errors='ignore', binary=True)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    result = {}
    try:

        event = json.loads(req)
        concepts = similar.find_similar(event['cui'], int(event['topn']))
        result = {
            "cui": event['cui'],
            "topn": event['topn'],
            "cuis": concepts
        }

    except:
        result = {}

    return json.dumps(result)



