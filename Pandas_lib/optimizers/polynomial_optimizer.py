import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def error_poly(C, data):
    # C: numpy.poly1d object or equivalent array representing polynomial coefficients
    # data: 2D array where each row is a point (x, y)
    # returns sum of squared error between polynomial and data
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err

def fit_poly(data, error_func, degree=3):
    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))
    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")
    # Call optimizer to minimize error function
    result = opt.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)  # convert optimal result into a poly1d object and return

def test_run():
    # Define original polynomial
    p_orig = np.float32([1.5, -10, -5, 60, 50])
    print("Original polynomial: {}".format(np.poly1d(p_orig)))
    Xorig = np.linspace(-5, 5, 21)
    Yorig = np.polyval(p_orig, Xorig)
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original polynomial")

    # Generate noisy data points
    noise_sigma = 30.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit a line to this data
    p_fit = fit_poly(data, error_poly)
    print("Fitted polynomial: {}".format(np.poly1d(p_fit)))
    plt.plot(data[:, 0], np.polyval(p_fit, data[:, 0]), 'r--', linewidth=2.0, label="Fitted polynomial")

    # Add a legend and show plot
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    test_run()