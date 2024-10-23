import json
import numpy as np
import math

test = []
 


# for i in range(1000):
#     entry = {
#     "System": "",
#     "x": np.random.normal() * 125,
#     "y": np.random.normal() * 50,
#     "Map": ""}
#     test.append(entry)

# with open("test.json", "w") as outfile:
#     json.dump(test, outfile)

with open('test2.json', 'r') as file:
    data = json.load(file)

# with open('data.json', 'r') as file:
#     data = json.load(file)
for entry in data:
    print("hi")
    if entry['x'] < -150:
        data.remove(entry)
        continue
    elif entry['x'] > 150:
        data.remove(entry)
        continue
    elif entry['y'] > 60:
        data.remove(entry)
        continue
    elif entry['y'] < -60:
        data.remove(entry)
        continue
    elif math.dist([0,0],[entry['x'],entry['y']]) > 100:
        data.remove(entry)
        continue
print(len(data))
with open("test2.json", "w") as outfile:
    json.dump(data, outfile)