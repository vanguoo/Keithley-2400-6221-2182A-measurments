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



class pdelta():
    def animate(self, i):
        data = pd.read_csv('%s' % filename)
        y = data['volt']
        x = data['time']
        self.ax2.cla()
        self.ax2.plot(x, y, marker='*',label='volt')
        
        self.ax2.legend()

    def live_plot(self,amp,width):

        amp1 = [amp,amp]
        width1 = [width,width]
        fig = plt.figure(figsize=(13, 6))
        plt.style.use('ggplot')
        # self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot()
        # self.ax1.plot(width1,amp1,label='amp-width')
        # self.ax1.set_xlabel('width')
        # self.ax1.set_ylabel('amp')
        # self.ax1.legend()
        ani = FuncAnimation(fig, self.animate,interval=10)
        plt.show()

    def setup(self,phigh=1e-6,plow=0,width=100e-6,times=1000,sdel=55e-6):
        rm = visa.ResourceManager("@py")
        instr1 = rm.open_resource('GPIB0::7::INSTR')
        # instr1 = rm.open_resource('TCPIP0::169.254.103.252::1394::SOCKET', write_termination='\r', read_termination='\n')


        instr1.write('*rst')
        instr1.write('unit v')
        
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

        flag= True
        times = int(times)
        time.sleep(3)
        while times:
            start = time.perf_counter()
            temp = instr1.query('sens:data?')
            stop = time.perf_counter()
            print('time is {}'.format(stop-start))
            times -= 1
        instr1.write('sour:swe:abor')

            # temp = temp+'\n'
            
            # with open('%s' % filename ,'a') as file2:
            #     file2.write(temp)
def initial_csv_62():
    feildname = ['volt','time']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    temp = time.ctime().replace(' ','_')
    filename = temp.replace(':','_')
    filename = '{}/{}.csv'.format(directory,filename)

    with open('%s' % filename,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename

if __name__ == "__main__":
    
    count = None
    xval = None
    yval = None
    global filename
    filename = initial_csv_62()
    sample = pdelta()
    t1 = threading.Thread(target=sample.live_plot,args=(1e-3,50e-6))
    t2 = threading.Thread(target=sample.setup)
    t2.start()
    t1.start()
    # t1.join()
    # t2.join()
    print('all done!')
    







