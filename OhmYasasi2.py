import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.interpolate import UnivariateSpline
from scipy import interpolate
from numpy import linspace, sin, pi
from scipy.interpolate import BPoly, CubicSpline
import scipy


plt.style.use('fast')

#x ve y eksenindeki veriler
x = np.array([1.04, 1.53, 2.03, 2.53, 3.03, 3.50, 4.00, 4.51, 5.04])
y = np.array([2.02, 2.55, 3.10, 3.60, 4.15, 4.50, 5.12, 5.65, 6.25])

#Renkler
colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])
#Marker
markers = ["o","o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.01
x_error = 0.01

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=100)

plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#spline
X_Y_Spline = interpolate.CubicSpline(x, y)
X_ = np.linspace(1.04,5.04)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_, c = 'black')

#Türev
spl = UnivariateSpline(x,y)
der = spl.derivatives(4)  #Burada sayıları tek tek girerek aldım
print(der)

plt.text(1.35, 4.50, 'Nokta - Eğim \n  2       1.04\n  2.5    1.01\n  3       0.99\n  3.5    1.01\n  4       1.05  ' + " ", size=12)
plt.title("Akım (I) - Gerilim (V) Grafiği")
plt.xlabel("V (Volt)")
plt.ylabel("I (mA)")
plt.grid(False)
print(plt.style.available) #Stilleri bastırıyor
plt.show()
