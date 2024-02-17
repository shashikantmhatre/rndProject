import json

from language.Executor import Executor
from language.context.ContextManager import ContextManager
from language.context.Data import Data
from language.initializer.Initializer import Initializer

algo = {
    "Policy": {
        "Premium": "Premium = 0 foreach veh in Vehicle do Premium = Premium + veh.Premium end ",
        "Term": "Term = 0.5",
        "TermPremium": "TermPremium = Premium * Term"
    },
    "Vehicle": {
        "Premium": "Premium = 100"
    }
}

def main():
    Initializer()

    with open("personal_auto_data.json") as f:
        nested_json = f.read()

    # Parse JSON string to a Python dictionary
    data = json.loads(nested_json)

    contextmanager = ContextManager()
    contextmanager.getmemory().add("__current", Data(data["Policy"], "Policy"))
    contextmanager.getmemory().add("__algo", algo)
    contextmanager.getmemory().add("__root", Data(data, "Root"))

    Executor(contextmanager, algo["Policy"]["TermPremium"]).process()
    print(data)


if __name__ == '__main__':
    main()
