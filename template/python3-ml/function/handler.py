import json
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
