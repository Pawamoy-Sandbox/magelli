#!/usr/bin/python
#-*- coding:utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys
import io

x, y = np.genfromtxt('diff.csv', delimiter=',').T
plt.plot(x, '-', label='Premiere acquisition')
plt.plot(y, '-', label='Seconde acquisition')
plt.xlabel("Combinaisons")
plt.ylabel("Temps")
plt.title('Mesures de temps')
plt.legend(loc='best')
plt.show()
