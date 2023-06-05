import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

#x ve y eksenindeki veriler
y = np.array([0.722, 2.688, 1.285, 5.155])
x = np.array([1.274, 5.102, 2.597, 10.40])

colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

markers = ["o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.00001
x_error = 0

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=150)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2,)

plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#fonskiyonu grafiğe bastırma
plt.text(1.05, 3.25, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=17)
#eğimi grafiğe bastırma
plt.text(1.05, 3.20, 'eğim =  {:.3f}'.format(a) + " Ω mm", size=17)

plt.title("R- l/A Grafiği")
plt.xlabel("l/A (1/mm)")
plt.ylabel("R (Ohm)")
plt.tight_layout()
plt.grid(True)
print(plt.style.available)

plt.show()
