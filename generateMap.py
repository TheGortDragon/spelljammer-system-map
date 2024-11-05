import json
import numpy as np
import math
import random

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

# with open('test2.json', 'r') as file:
#     data = json.load(file)

# # with open('data.json', 'r') as file:
# #     data = json.load(file)
# for entry in data:
#     print("hi")
#     if entry['x'] < -150:
#         data.remove(entry)
#         continue
#     elif entry['x'] > 150:
#         data.remove(entry)
#         continue
#     elif entry['y'] > 60:
#         data.remove(entry)
#         continue
#     elif entry['y'] < -60:
#         data.remove(entry)
#         continue
#     elif math.dist([0,0],[entry['x'],entry['y']]) > 100:
#         data.remove(entry)
#         continue
# print(len(data))
# with open("test2.json", "w") as outfile:
#     json.dump(data, outfile)

with open('testData.json', 'r') as file1:
    data = json.load(file1)

with open('sysNames.json', 'r') as file2:
    nameData = json.load(file2)

for entry in data:
    idx = random.randrange(1, len(nameData), 1)
    entry['System'] = nameData[idx]['name']
    print(nameData[idx]['name'])
    nameData.remove(nameData[idx])


# filtered_nameData = [entry for entry in nameData if not any(str(i) in entry['name'] for i in range(10))]
# print(len(nameData))
# for entry in nameData:
#     for i in range(10):
#         if (entry['name'].find(str(i)) != -1):
#             nameData.remove(entry)
#             break
# print(len(filtered_nameData))
with open("testData.json", "w") as outfile:
    json.dump(data, outfile)