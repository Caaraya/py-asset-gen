
from gen_blop import *
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_aspect("equal")

rad = 0.2
edgy = 0.05

for c in np.array([[0,0], [0,1], [1,0], [1,1]]):

    a = get_random_points(n=7, scale=1) + c
    x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
    plt.plot(x,y)

plt.axis('off')
plt.savefig("blops.png", bbox_inches='tight', transparent=True)