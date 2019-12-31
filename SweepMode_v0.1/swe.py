from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import csv
import time
import threading
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

data1 = None
filename = None
count  = None

class mes():

    def animate(self,i,):
        global count
        data1 = pd.read_csv('%s.csv' % filename)
        x = data1['voltage']
        y = data1['current']
        z = data1['resistance']
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
        
        
        if count!=5:
            count +=1
            print(count)

        print('ok')
        #一秒更新一次所以，
        
        

    def live_plot(self,filename_para):
        global filename
        global data1
        global count

        filename = filename_para
        fig = plt.figure(figsize=(13, 6))
        plt.style.use('ggplot')
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        self.ax1.cla()
        self.ax2.cla()
        count = 1
        ani = FuncAnimation(fig, self.animate, interval=1000)
        plt.show()
        plt.savefig('%s.png'% filename)
        

    def sweep_mode(self,a=-0.5,b=0.5,c=0.1,cmpl=100e-3):
        
        rm = visa.ResourceManager('@py')
        instr = rm.open_resource('GPIB0::24::INSTR')
        instr.write('*rst')
        instr.write(':outp on')
        instr.write(':sour:func volt')
        instr.write(':sens:curr:prot %s' % cmpl)
        instr.write(':sens:func "curr:dc"')
        
        i = a
        flag = True
        while (flag):
            instr.write(':sour:volt:lev %s' % i)
            instr.write(':read?')
            time.sleep(1)
            data = instr.read()

            list_data = data.split(',')
            list_data.pop()
            resistance = float(list_data[0])/float(list_data[1])
            list_data.append('%s\n' % resistance)
            data1 = ','.join(list_data)
            print(data1)

            with open('%s.csv' % filename, 'a') as file:
                file.write(data1)
                print(filename)
            i += c
            x = round(i, 2)

            if x == b:
                flag = False
                instr.write(':outp off')

if __name__ == "__main__":
    temp = mes()
    temp.live_plot('van/1')
    # a =mes.live_plot(filename_para=1,stop_it=)





















