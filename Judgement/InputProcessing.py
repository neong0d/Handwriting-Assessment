"""
Given a .json file containing coordinates of input drawn on canvas as:

{'x': 211, 'y': 301.2},
{'x': 211, 'y': 301.2},
...
{'x': 214, 'y': 300.2},
{'x': 216, 'y': 297.2},

with arbitrary number of points and scale,
scale & normalise it to 90 points of desired frame size.
"""

import numpy as np
import matplotlib.pyplot as plt
import json

def scale(x, y):
    ideal_x_size = 449
    ideal_y_size = 460
    max_x = max(x)
    max_y = max(y)
    min_x = min(x)
    min_y = min(y)
    aspect_ratio = 1 # max_y/max_x

    scale_x = ideal_x_size/(3*(max_x - min_x))
    scale_y = ideal_y_size/(3*(max_y-min_y))
    max_x *= scale_x
    min_x *= scale_x
    max_y *= scale_y
    min_y *= scale_y

    # frame normalization
    new_x = [i * scale_x for i in x]
    new_y = [i * scale_y for i in y]

    return new_x,new_y


def normalize(x, y):
    ideal_count = 89
    new_x, new_y = [x[02]], [y[0]]
    for i in range(len(x)-1):
        dist = (x[i] - x[i+1]) ** 2 + (y[i] - y[i+1])**2
        if dist > 0:
            new_x.append(x[i+1])
            new_y.append(y[i+1])
    #x,y = original
    x1,y1 = [], []
    x1.append(new_x[0])
    y1.append(new_y[0])

    index, len_original = 1, len(new_x)

    v = len_original/ideal_count
    if len_original < ideal_count: 
        x1[len_original:ideal_count] = x1[len_original-1]
    else:
        for i in range(0,ideal_count):
            v6 = (len_original/ideal_count) * i
            if v6 <= len_original:
                x1.append(new_x[int(v6)])
                y1.append(new_y[int(v6)])

    return x1,y1

if __name__=='__main__':
    with open('points.json', 'r') as file:
        data = json.load(file)
        x = [i['x'] for i in data]
        y = [i['y'] for i in data]
        scaled = scale(x, y)
        normalized = normalize(scaled[0], scaled[1])

        #display input image & scaled 90-point image
        showplot(x, y)
        showplot(normalized[0], normalized[1])