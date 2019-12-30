import matplotlib.pyplot as plt
import pandas as pd
import time



data = pd.read_csv('6221/g.csv')
x = data['time']
z = data['res']
print(x)
print(z)

plt.plot(x,marker='*',label='time-resistance')
plt.legend()
plt.show()
