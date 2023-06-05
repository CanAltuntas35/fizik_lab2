
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

#x ve y eksenindeki veriler
x = np.array([4.5, 9.0, 13.6, 18.0, 22.5, 27.1, 31.5, 36.1, 40.6, 45.0])
y = np.array([1.01, 2.01, 3.03, 4.01, 4.99, 6.01, 7.01, 8.01, 9.02, 10.00])

#x ve y eksenindeki veriler
j = np.array([3.1, 6.2, 9.3, 12.3, 15.3, 18.5, 21.6, 24.7, 27.7, 30.9])
k = np.array([1.01, 2.02, 3.04, 4.02, 5.00, 6.02, 7.01, 8.03, 9.00, 10.03])

#x ve y eksenindeki veriler
o = np.array([2.1, 4.3, 6.4, 8.5, 10.7, 12.8, 14.9, 17.1, 19.2, 21.4])
p = np.array([1.01, 2.02, 3.04, 4.02, 5.01, 6.02, 7.02, 8.04, 9.00, 10.05])

markers = ["o","o","o","o","o","o","o","o","o","o"]
colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=150)

for ji,ki, m2, c2 in zip(j,k,markers, colors):
    plt.scatter(ji, ki, c=c, marker=m, s=150)

for oi,pi, m3, c3 in zip(o,p,markers, colors):
    plt.scatter(oi, pi, c=c, marker=m, s=150)


#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu bulma polyfit buluyor
c, d = np.polyfit(j, k, 1)

#en iyi doğruyu bulma polyfit buluyor
t, y = np.polyfit(o, p, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2, label= "R1")

#en iyi doğruyu çizdirme
plt.plot(j, c*j+d, color='green', linestyle='-', linewidth=2, label = "R2")

#en iyi doğruyu çizdirme
plt.plot(o, t*o+y, color='red', linestyle='-', linewidth=2, label = "R3")

plt.legend(loc = "upper left")

#fonskiyonu grafiğe bastırma
plt.text(0.090, 7.75, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=12)
#eğimi grafiğe bastırma
plt.text(0.090, 7.70, 'R1 eğim =  {:.3f}'.format(a) + " V/mA", size=12)

#fonskiyonu grafiğe bastırma
plt.text(0.090, 6.75, 'y = ' +  '{:.3f}'.format(c) + 'x' + ' + {:.2f}\n'.format(d), size=12)
#eğimi grafiğe bastırma
plt.text(0.090, 6.70, 'R2 eğim =  {:.3f}'.format(c) + " V/mA", size=12)

#fonskiyonu grafiğe bastırma
plt.text(0.090, 5.75, 'y = ' +  '{:.3f}'.format(t) + 'x' + ' + {:.2f}\n'.format(y), size=12)
#eğimi grafiğe bastırma
plt.text(0.090, 5.70, 'R3 eğim =  {:.3f}'.format(t) + " V/mA", size=12)


plt.title("I (mili Amper) - V (Volt) Grafiği")

plt.xlabel("I (mA)")

plt.ylabel("V (V)")

plt.tight_layout()

plt.grid(True)

print(plt.style.available)

plt.show()
