
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

#x ve y eksenindeki veriler
x = np.array([np.tan(np.deg2rad(32.37)), np.tan(np.deg2rad(51.72)), 
                np.tan(np.deg2rad(62.25)), np.tan(np.deg2rad(68.47)), 
                    np.tan(np.deg2rad(72.48)), np.tan(np.deg2rad(75.26)),
                        np.tan(np.deg2rad(77.29)),np.tan(np.deg2rad(78.84)),
                            np.tan(np.deg2rad(80.05))])

y = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

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
plt.text(0.7, 148.55, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=17)
#eğimi grafiğe bastırma
plt.text(0.7, 148.50, 'eğim =  {:.3f}'.format(a) + " 1/mA", size=17)


plt.title("tan(a) - Akım Grafiği")

plt.xlabel("I (mA)")

plt.ylabel("tan(a)")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()


print(plt.style.available)

plt.show()
