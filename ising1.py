import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint as randint

# sign convention:
# H = - sum(i, j) J_(i, j)*S[i]*S[j] - sum(i) B*S[i]
# in symbolic notation. i above is actually 2-dim index (i, j)
# sum for j is taken for all adjacent neighbors of i

N = 10
n_step = 10000

beta = 0.1
B = 0
J = 1.0

spins = randint(2, size=(N, N), dtype=int)
spins = 2*spins - 1

def display(fig, spins):
    print('-'*N)
    for i in range(N):
        s = ''
        for j in range(N):
          s += 'o' if spins[i][j] == 1 else '+'
        print(s)

np.random.seed(int(time.time()))

i, j = 0, 0
for step in range(n_step):
    (i, j) = ((step // N) % N, step % N)

    left = spins[i][j-1] if j >= 1 else -1
    right = spins[i][j+1] if j < N - 1 else -1
    up = spins[i - 1][j] if i >= 1 else -1
    down = spins[i + 1][j] if i < N - 1 else -1
    g =  (left + right + up + down)
    neg_delta_H = -2 * spins[i][j] * (g * J  + B)
    r = np.exp(beta * neg_delta_H) if neg_delta_H < 0 else 1
    s = np.random.uniform()
    # if step % (n_step / 10)  == 0 and (i, j) == (0, 0):
    #     print('spins[%d][%d] = %d'%(i, j, spins[i][j]))
    #     print('l, r, u, d = %d, %d, %d, %d' % (left, right, up, down))
    #     print('g = %d, -dH = %f, r = %f, s = %f' % (g, neg_delta_H, r, s))
    if s < r:
        spins[i][j] *= -1
    if step % (n_step / 10)  == 0:
        average = np.sum(spins)/(N*N)
        display(None, spins)
        print("step %d, average = %f" % (step, average))

print('run %d step, average = %f' % (n_step, average))
