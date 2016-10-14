import yaml
import json

d = {1:2, "a": "Blah"}
l = [ 5, "apple", d, 6 ]

with open ("blah.yml", "w") as F:
    yaml.dump(l, F, default_flow_style=False)

with open("blah.json", "w") as F:
    json.dump(l, F)

