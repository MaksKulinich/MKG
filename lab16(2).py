import pylab
import numpy as np
import json
file = open("Regions.txt", "rb")
slovn_json = json.load(file)
print(slovn_json)
x = slovn_json.keys()
y = slovn_json.values()
pylab.bar(x,y)
pylab.show()