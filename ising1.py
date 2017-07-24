import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint as randint

# sign convention:
# H = - sum(i, j) J_(i, j)*S[i]*S[j] - sum(i) B*S[i]
# in symbolic notation. i above is actually 2-dim index (i, j)
N = 10
n_step = 10000

beta = 0.25
b = 0.0
j = 1.0

spins = randint(2, size=(N, N), dtype=int)
spins = 2*spins - 1

# magnetic field (bias)
# B = np.full((N, N), b)

# spin-spin coupling, horizontal and vertical
# J_h = np.full((N, N - 1), j)
# J_v = np.full((N - 1, N), j)

# print(spins)
# print("B =\n%s\n J_h =\n%s\n J_v =\n%s"%(B, J_h, J_v))

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

    left = spins[i][j-1] if j >= 1 else 0
    right = spins[i][j+1] if j < N - 1 else 0
    up = spins[i - 1][j] if i >= 1 else 0
    down = spins[i + 1][j] if i < N - 1 else 0
    g =  (left + right + up + down)
    neg_delta_H = -2 * spins[i][j] * (g * j  + b)
    r = np.exp(beta * neg_delta_H) if neg_delta_H < 0 else 1
    # print('-dH = %f, beta * (-dH) = %f, r = %f' %
    #       (neg_delta_H, beta * neg_delta_H, r))
    # print("r = %f" % r)
    s = np.random.uniform()
    if s < r:
        spins[i][j] *= -1
    if step % (n_step / 10)  == 0:
        average = np.sum(spins)/(N*N)
        display(None, spins)
        print("step %d, average = %f" % (step, average))

print('run %d step, average = %f' % (step, average))
