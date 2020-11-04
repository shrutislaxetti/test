import json
from random import choice
from string import ascii_lowercase, digits
 
def check_read_params():
    try:
        with open("""../iam-policies/iam-policy.json""", 'r') as f:
            policy = json.load(f)
            return json.dumps(policy)
    except Exception as ex:
        print(ex)
        return ""

def write_param_file():
    policy = check_read_params()
    obj = {
        "Parameters": {
            "Policy" : ""
        }
    }
    if policy is not False:
        outjson = str(policy).replace('\r', '')
        obj["Parameters"]["Policy"] = outjson
        print(obj)
        try:
            with open("""../parameters/attach-policy.json""", 'w') as f:
                json.dump(obj, f)
        except Exception as ex:
            print(ex)
            return False

write_param_file()
