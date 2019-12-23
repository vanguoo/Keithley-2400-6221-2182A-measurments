import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import swe

class liveplot_2400():
    def __init__(self):
    
        self.fig = plt.figure(figsize=(13, 6))
        style.use('ggplot')
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        self.live_plot()

    def animate(self, i):
        
        x = self.data['value1']
        y = self.data['value2']
        z = self.data['resistance']

        self.ax1.cla()
        self.ax2.cla()
        self.ax1.plot(x, y, marker='o', label='V-I')
        self.ax2.plot(x, z, marker='*', label='resistance')

        self.ax1.set_xlabel('voltage')
        self.ax1.set_ylabel('current')
        self.ax2.set_xlabel('voltage')
        self.ax2.set_ylabel('resistance')
        self.ax1.legend()
        self.ax2.legend()

    def live_plot(self):
        ani = FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()




