import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fast')

#x ve y eksenindeki veriler
x = np.array([1.0, 2.07, 3.02, 4.01, 5.02, 6.00, 7.02, 8.01, 9.05, 10.03])
y = np.array([2.12, 4.40, 6.42, 8.54, 10.69, 12.77, 14.92, 17.04, 19.23,21.30])

colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

markers = ["o","o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.01
x_error = 0.01

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=100)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2,)

plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#fonskiyonu grafiğe bastırma
plt.text(2.01, 17.85, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=13)
#eğimi grafiğe bastırma
plt.text(2.01, 17.80, 'eğim =  {:.3f}'.format(a) + " mA / V", size=13)

plt.title("Akım (I) - Gerilim (V) Grafiği")

plt.xlabel("V (Volt)")

plt.ylabel("I (mA)")

plt.grid(True)

plt.tight_layout()

print(plt.style.available)

plt.show()
