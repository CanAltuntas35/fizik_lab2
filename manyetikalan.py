
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

#x ve y eksenindeki veriler
x = np.array([0.1, 0.075, 0.06, 0.05])
y = np.array([0.0011, 0.00057, 0.00049, 0.00038])

colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

markers = ["o","o","o","o","o","o","o","o","o"]

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=100)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2,)

#fonskiyonu grafiğe bastırma
plt.text(0.7, 1.55, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=17)
#eğimi grafiğe bastırma
plt.text(0.7, 1.50, 'eğim =  {:.3f}'.format(a) + " m/s", size=17)


plt.title("Manyetik Alan - Akım Grafiği")

plt.xlabel("")

plt.ylabel("")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()


print(plt.style.available)

plt.show()
