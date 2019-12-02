import matplotlib.pyplot as plt
import numpy as np
from gen_blop import *
import math
import json

def get_pivot_points(x,y,piv):
  pivx = round(len(x)/piv)
  pivy = round(len(y)/piv)
  data_points = []
  for i in range(piv):
    data_points.append([x[i*pivx], y[i*pivy]])
  return data_points


def avg(arr):
  return sum(arr) / len(arr)

def nearest_sq(n):
  return round(math.sqrt(n))

def get_quadranted_array(nodes):
    r,l = 0,0
    n_sq = nearest_sq(nodes)
    arr = []
    for i in range(nodes):
      arr.append([l,r])
      if (r == n_sq - 1):
        l += 1
        r = 0
      else:
        r += 1
    return arr

def save_blop(np_size=7, rand_points=7, scale=1, rad=0.2, edgy=0.05, name="blops", pivot_points=5):
  fig, ax = plt.subplots()
  ax.set_aspect("equal")
  data = {}
  data['shape'] = []

  for c in get_quadranted_array(np_size):

      a = get_random_points(n=rand_points, scale=scale) + c
      x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
      x_mid, y_mid = avg(x), avg(y)
      pivots = get_pivot_points(x,y,pivot_points);
      plt.fill(x,y)
      data['shape'].append({'center': [x_mid,y_mid], 'quadrant': c, 'pivots': pivots})
      #plt.plot([x_mid], [y_mid], color='k',marker='o',lw=0, linestyle="")
      #for p in pivots:
      #  plt.plot([p[0]], [p[1]], color='w', marker='o', lw = 0, linestyle="")

  plt.axis('off')
  plt.savefig(name + ".png", bbox_inches='tight', transparent=True)
  with open(name + ".json", 'w') as outfile:
    json.dump(data, outfile)