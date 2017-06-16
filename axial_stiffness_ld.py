__author__ = 'Matej'

import numpy as np
import matplotlib.pyplot as plt

a_0 = [-30, -7222]
a = [30, 7222]
b = [100, 12927]
c = [1000, 49513]
a1 = [30, 2606]
b1 = [100, 6385]
c1 = [1000, 34932]
d = [a_0, a, b, c]
d1 = [a1, b1, c1]

xticks = np.arange(0, 1020, 100)
yticks = np.arange(0, 5e4+100, 1e4)

plt.figure('Axial stiffness - load dependency', figsize=(14, 5))
plt.rcParams.update({'font.size': 28, 'text.usetex': True})
plt.plot([col[0] for col in d], [col[1] for col in d], 'o-')
#plt.plot([col[0] for col in d1], [col[1] for col in d1], 'o-')
plt.xlim([0, 1015])
plt.ylim([0, 5.2e4])
plt.xlabel('$F\,\,\mathrm{[N]}$')
plt.ylabel('$k_{zz}\,\,\mathrm{[N/mm]}$')
plt.xticks(xticks)
plt.yticks(yticks)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
#ax1.set_xticks(major_ticks)
plt.grid()
plt.tight_layout(pad=0.1)
plt.savefig('c:/Users/Matej/Documents/_FS_3.1/_podiplomski_izpiti/seminar_1/latex/testbench/ld.pdf')
plt.show()
