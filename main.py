# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import datetime as dt

for i in range(2):
    A = np.random.rand(20000, 20000)
    B = np.random.rand(20000, 20000)

    C = np.dot(A, B)
    now = dt.datetime.now()
    print(C)
    print(i)
    print(now)