import matplotlib.pyplot as plt
import numpy as np
from gen_blop import *
import math

def save_blop(np_size=7, rand_points=7, scale=1, rad=0.2, edgy=0.05, name="blops"):
  fig, ax = plt.subplots()
  ax.set_aspect("equal")

  r,l = 0,0
  nearest_sq = round(math.sqrt(np_size))
  arr = []
  for i in range(np_size):
    arr.append([l,r])
    if (r == nearest_sq - 1):
      l += 1
      r = 0
    else:
      r += 1
  print(arr)

  for c in arr:

      a = get_random_points(n=rand_points, scale=scale) + c
      x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
      plt.fill(x,y)

  plt.axis('off')
  plt.savefig(name + ".png", bbox_inches='tight', transparent=True)