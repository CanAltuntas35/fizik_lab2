
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-deep')

#x ve y eksenindeki veriler
x = np.array([26, 52, 80])
y = np.array([4, 8, 12])

#x ve y eksenindeki veriler
j = np.array([2,4,6])
k = np.array([4, 8, 12])


#x ve y eksenindeki veriler
o = np.array([2.3, 4.6, 7])
p = np.array([4, 8, 12])



colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

markers = ["o","o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.00001
x_error = 0

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=50)

for ji,ki, m2, c2 in zip(j,k,markers, colors):
    plt.scatter(ji, ki, c=c, marker=m, s=50)

for oi,pi, m3, c3 in zip(o,p,markers, colors):
    plt.scatter(oi, pi, c=c, marker=m, s=50)



#hepsi için en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

c, d = np.polyfit(j, k, 1)

t, y = np.polyfit(o, p, 1)


#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2, label= "R1")

#en iyi doğruyu çizdirme
plt.plot(j, c*j+d, color='black', linestyle='-', linewidth=2, label = "R2")

#en iyi doğruyu çizdirme
plt.plot(o, t*o+y, color='black', linestyle='-', linewidth=2, label = "R3")

#fonskiyonu grafiğe bastırma
plt.text(15.05, 10.75, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=10)
#eğimi grafiğe bastırma
plt.text(15.05, 10.70, 'R1 eğim =  {:.3f}'.format(a) + " V/mA", size=10)

#fonskiyonu grafiğe bastırma
plt.text(15.05, 8.75, 'y = ' +  '{:.3f}'.format(c) + 'x' + ' + {:.2f}\n'.format(d), size=10)
#eğimi grafiğe bastırma
plt.text(15.05, 8.60, 'R2 eğim =  {:.3f}'.format(c) + " V/mA", size=10)

#fonskiyonu grafiğe bastırma
plt.text(15.05, 6.75, 'y = ' +  '{:.3f}'.format(t) + 'x' + ' + {:.2f}\n'.format(y), size=10)
#eğimi grafiğe bastırma
plt.text(15.05, 6.60, 'R3 eğim =  {:.3f}'.format(t) + " V/mA", size=10)



plt.title("Akım - Gerilim Grafiği")

plt.xlabel("Akım (mA)")

plt.ylabel("Gerilim (V)")

plt.tight_layout()

plt.grid(True)

print(plt.style.available)

plt.show()
