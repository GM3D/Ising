import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint as randint

# sign convention:
# H = - sum(i, j) J_(i, j)*S[i]*S[j] - sum(i) B*S[i]
# in symbolic notation. i above is actually 2-dim index (i, j)
# sum for j is taken for all adjacent neighbors of i
class Ising:
    def __init__(self, N, n_step, beta, B, J):
        self.N = N
        self.n_step = n_step
        self.steps_run = 0
        self.beta = beta
        self.B = B
        self.J = J
        np.random.seed(int(time.time()))
        self.spins = randint(2, size=(self.N, self.N), dtype=int)
        self.spins = 2*self.spins - 1

    def average(self):
        return np.sum(self.spins) / (self.N * self.N)

    def display(self):
        print('-'*N)
        for i in range(N):
            s = ''
            for j in range(N):
                s += 'o' if self.spins[i][j] == 1 else '+'
            print(s)

    def adj_sum(self, i, j):
        left = self.spins[i][j-1] if j >= 1 else -1
        right = self.spins[i][j+1] if j < N - 1 else -1
        up = self.spins[i - 1][j] if i >= 1 else -1
        down = self.spins[i + 1][j] if i < N - 1 else -1
        return left + right + up + down
        
    def run(self, n_step=0, display=False):
        if not n_step:
            n_step = self.n_step
            half_step = n_step // 2
            long_range_order = 0.0
        for step in range(n_step):
            (i, j) = ((step // self.N) % self.N, step % self.N)
            neg_delta_H = -2 * self.spins[i][j] * (self.adj_sum(i, j) * J  + B)
            r = np.exp(self.beta * neg_delta_H) if neg_delta_H < 0 else 1
            s = np.random.uniform()
            if s < r:
                self.spins[i][j] *= -1
            if display and (step % (self.n_step / 10)  == 0):
                self.display()
                print("step %d, average = %f" % (step, self.average()))
            if step >= half_step:
                long_range_order += self.average()
            self.steps_run = step + 1
            self.long_range_order = long_range_order / (n_step - half_step)
            
    def report(self):
        print('N = %d, n_step = %d, beta = %f, B = %f, J = %f' %
              (self.N, self.n_step, self.beta, self.B, self.J))
        print('run %d step, average = %f' %
              (self.steps_run, self.long_range_order))

if __name__ == '__main__':    
    N = 10
    n_step = 10000
    beta = 2.0
    B = 0
    J = 1.0
    ising = Ising(N, n_step, beta, B, J)
    ising.run()
    ising.report()


