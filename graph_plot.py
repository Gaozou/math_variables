import matplotlib.pyplot as plt
import numpy as np

k = 2
x = np.linspace(-2,2,100)

fig, ax = plt.subplots()
ax.plot(x, k*x, label='$F=kx, k=2$[N/m]')
ax.set_xlabel('x[m]')
ax.set_ylabel('F[N]')
ax.grid()
ax.legend()

plt.savefig('graphics/fook_graph.pdf')

print('done')