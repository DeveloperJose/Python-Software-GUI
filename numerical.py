import numpy as np
def f(x):
    return np.arctan((100*(x**2)) - (199*x) + 100)

def fprime(x):
    return ((200*x)-199)/((((100*(x**2))-(199*x)+100)**2)+1)

def dh_forward(x, h):
    return (f(x+h) - f(x)) / h

x = 1
for n in range(0, 25):
    h = 0.1/(2**n)
    n_deriv = dh_forward(x, h)
    deriv = fprime(x)
    error = (n_deriv - deriv) / deriv
    print("Forward %.2f, True %.2f, Error %.2f" % (n_deriv, deriv, error))