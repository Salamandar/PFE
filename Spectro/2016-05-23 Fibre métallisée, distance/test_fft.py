#"2016-05-23 metal metal air d1.tsv"
#"2016-05-23 metal metal air d2.tsv"
#"2016-05-23 metal metal air d3.tsv"
#"2016-05-23 metal metal air d4.tsv"
#"2016-05-23 metal metal air d5.tsv"


#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


x,y = np.loadtxt("2016-05-23 metal metal air d1.tsv", unpack=True)

N = len(x)
print("number of points :", N)

T = (820-350)/3390

yf = scipy.fftpack.fft(y)
Nf = len(yf)
xf = np.linspace(0.0, 1.0/(2.0*T), N)

fig, ax = plt.subplots()
plt.plot(xf, yf)
plt.show()
