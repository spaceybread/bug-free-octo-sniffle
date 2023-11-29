from matplotlib import pyplot as plt

xs = []
ys = []

a = int(input())
b = int(input())

for i in range(1000):
   x = i / 100 - 5
   y = (x**3 + x*a + b)

   if y >= 0: 
      yu  = (x**3 + x*a + b)**0.5
      yd = -1 * yu
      xs.append(x)
      ys.append(yu)
      xs.append(x)
      ys.append(yd)
plt.scatter(xs, ys)
plt.xlim(-6,6)
plt.ylim(-6, 6)
plt.show()
