import yaml
import json
from pprint import pprint as pp

with open ("blah.yml") as F:
    l = yaml.load(F)
pp(l)

with open("blah.json") as F:
    l = json.load(F)
pp(l)

