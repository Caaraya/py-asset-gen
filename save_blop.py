import matplotlib.pyplot as plt
import numpy as np
from gen_blop import *
import math

def get_quadranted_array(nodes):
    r,l = 0,0
    nearest_sq = round(math.sqrt(nodes))
    arr = []
    for i in range(nodes):
      arr.append([l,r])
      if (r == nearest_sq - 1):
        l += 1
        r = 0
      else:
        r += 1
    return arr

def save_blop(fig_size=15, np_size=7, rand_points=7, scale=1, rad=0.2, edgy=0.05, name="blops"):
  fig, ax = plt.subplots(figsize=(fig_size, fig_size))
  ax.set_aspect("equal")

  for c in get_quadranted_array(np_size):

      a = get_random_points(n=rand_points, scale=scale) + c
      x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
      plt.fill(x,y)

  plt.axis('off')
  plt.savefig(name + ".png", bbox_inches='tight', transparent=True)