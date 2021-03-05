#!/bin/python3

import matplotlib.pyplot as plt
import loaddata as load

a = load.Col("/home/anton/saxs/saxs_results/2lpj_monomer_xtal/intensity.xvg", 1)
b = load.Col("/home/anton/saxs/saxs_results/2lpj_monomer_xtal/intensity.xvg", 2)

a = [i * 10 for i in a]

x = load.Col('waxs_final.xvg', 1)
y = load.Col('waxs_final.xvg', 2)

plt.plot(a, b, label="theoretical/online")
plt.plot(x, y, label="my own")

plt.yscale('log')
plt.axis([0, 10, 5*10**3, 4*10**6])
plt.legend()
plt.show()
