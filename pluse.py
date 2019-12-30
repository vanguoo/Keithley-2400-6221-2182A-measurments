from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import time
import threading
import matplotlib.pyplot as plt
import pandas as pd
import csv
import itertools
from matplotlib.animation import FuncAnimation
import numpy as np


class pdelta():
    def animate(self, i):
        data = pd.read_csv('%s' % filename)
        y = data['resistance']
        x = data['time']
        global count
        # y = np.random.randint(100)
        # if count<10:
        
        self.ax2.cla()
        self.ax2.plot(x, y, marker='*',label='resistance')
        
        self.ax2.set_xlabel('time')
        self.ax2.set_ylabel('resistance')
        
        self.ax2.legend()
        


    def live_plot(self,file_62,amp,width):
        global filename
        filename = str(file_62)
        global count
        global xval
        global yval
        
        amp1 = [amp,amp]
        width1 = [width,width]
        fig = plt.figure(figsize=(13, 6))
        plt.style.use('ggplot')
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        self.ax1.plot(width1,amp1,label='amp-width')
        self.ax1.set_xlabel('width')
        self.ax1.set_ylabel('amp')
        self.ax1.legend()
        
        print("liveplot has recevied it! %s" % filename)
        
        count = 1
        xval = []
        yval = []
        ani = FuncAnimation(fig, self.animate,interval=1000)
        plt.show()

        plt.savefig('%s.png' % filename)

    def task(self):
        count =10
        while 1:
            time.sleep(1)
            print('here is main thread ')
            count -=1
            if count==0:
                break
    

    def setup(self,phigh=1e-3,plow=0,width=100e-6,times=1000,sdel=16e-6):
        
        # phigh,plow,width,times,sdel = args
        print(phigh,plow,width,times)
        rm = visa.ResourceManager("@py")
        instr1 = rm.open_resource('GPIB0::7::INSTR')
        # instr1 = rm.open_resource('TCPIP0::169.254.211.198::1394::SOCKET', write_termination='\r', read_termination='\n')


        instr1.write('*rst')
        instr1.write('unit ohms')
        
        instr1.write('sour:pdel:high %s' % phigh)
        instr1.write('sour:pdel:low %s' % plow)
        instr1.write('sour:pdel:WIDT %s' % width)

        instr1.write('sour:pdel:SDEL %s' % sdel)
        # instr1.write('sour:pdel:coun ')
        instr1.write('sour:pdel:rang best')
        instr1.write('sour:pdel:int %s' % 5)
        instr1.write('sour:pdel:lme 2')
        instr1.write('sour:pdel:swe off')
        instr1.write('sour:pdel:arm')

        # instr1.write('sour:del 0.2')
        instr1.write('init')
        
        
        time1 = 1
        flag= True
        times = int(times)
        while times:
            temp = instr1.query('sens:data?')
            temp1 = temp.split(',')
            print(temp1)
            temp1.pop()
            temp1.append('%s\n' % time1)
            data  = ','.join(temp1)
            time1 +=1
            print(data)
            # with open('%s' % filename ,'a') as file2:
            #     file2.write(data)

            times -= 1

        instr1.write('sour:swe:abor')

def initial_csv_62():
    feildname = ['resistance','time']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    temp = time.ctime().replace(' ','_')
    filename = temp.replace(':','_')
    filename = '{}/{}.csv'.format(directory,filename)

    with open('%s' % filename,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename

if __name__ == "__main__":
    filename = None
    count = None
    xval = None
    yval = None
    sample = pdelta()
    sample.setup()
    # file62 = initial_csv_62()
    # t1 = threading.Thread(target=sample.live_plot,args=(file62,1e-3,50e-6))
    # t2 = threading.Thread(target=sample.setup)
    # t2.start()
    # t1.start()
    # t1.join()
    # t2.join()
    print('all done!')
    







