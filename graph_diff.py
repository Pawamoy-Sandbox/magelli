#!/usr/bin/python
#-*- coding:utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys
import io

x = np.genfromtxt('diff2.csv', delimiter=',').T
plt.plot(x, '-', label='Differences des acquisitions')
plt.xlabel("Combinaisons")
plt.ylabel("Temps")
plt.title('Ecart de temps')
plt.legend(loc='best')
plt.show()
