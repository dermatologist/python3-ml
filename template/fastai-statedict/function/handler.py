import json
import os
from pathlib import PurePath

# No warnings in production
import warnings
warnings.filterwarnings("ignore")


FUNCTION_ROOT = os.environ.get("function_root", "/root/function/")

# Load model here
# model = 

# fill in weights
Model.load_state_dict(
    torch.load(str(PurePath(FUNCTION_ROOT, "data/exported-state-dict.pt")))
)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    event = json.loads(req)
    concepts = my_function(event['var1'], int(event['var2']))
    result = {
        "var1": event['var1'],
        "var2": event['var2'],
        "var1s": concepts
    }

    return json.dumps(result)

def my_function(var1, var2):
    return model.my_task(var1, var2=tn)
