import visa
from gpib_ctypes import make_default_gpib
make_default_gpib()
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import threading
import time
import csv
import pandas as pd
from decimal import Decimal

rm = visa.ResourceManager('@py')
instr24 = rm.open_resource('GPIB0::24::INSTR')


def initial_csv_62():
    feildname = ['voltage','current','res','timestamp','statucode']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    # temp = time.ctime().replace(' ','_')
    # filename6 = temp.replace(':','_')
    filename6 = '{}.csv'.format(directory)
    with open('%s' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6

def pluse_2400_self(high_curr1 = 5e-3):
    
    i=30
    high_curr = str(high_curr1)
    temp2 = 0
    temp1 = 0
    rate = 0
    rate1 = 0
    count = 0
    count1 = 0
    instr24.write(':outp on')
    while i:
        j = temp2 + 40
        start_low = time.perf_counter()
        while j:
            
            instr24.write('sour:volt:lev 0.0000000')
            # instr24.write('init')
            temp4=instr24.query(':read?').split(',')
            temp4[2] = str(0)
            data_low = ','.join(temp4)
            with open('%s' % filename,'a') as file3:
                file3.write(data_low)
            j -=1
            
        count +=1
        stop_low = time.perf_counter()
        print(f'low time is {stop_low-start_low}')
        # temp2 += rate
        print(count)
        if count == 1:
            rate +=0
        rate +=40
        

        w = temp1 + 40
        start_low1 = time.perf_counter()
        while w:
            
            instr24.write('sour:volt:lev %s ' % high_curr)
            # instr24.write('init')
            temp = instr24.query(':read?').split(',')
            resistance = float(temp[0])/float(temp[1])
            temp[2] = str(resistance)
            data_hig = ','.join(temp)
            with open('%s' % filename,'a') as file4:
                file4.write(data_hig)
            w -=1
        count1 +=1
        stop_low1 = time.perf_counter()
        print(f'high time is {stop_low1-start_low1}')
        
        # temp1 += rate1
        if count1==1:
            rate1 += 0
        rate1 +=40

        i -=1
        print(i)
    instr24.write(':outp off')


def plot_24():
    global ax1
    global ax2
    global ax3
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    ani = FuncAnimation(fig,animate,interval=100)
    plt.show()

def animate(i):
    data = pd.read_csv('%s' % filename)
    x = data['timestamp']
    c = data['current']
    r = data['res']
    v = data['voltage']
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax1.plot(x,c,marker='o',label='time-current',color='b')
    ax2.plot(x,r,marker='*',label='time-resistance',color='r')
    ax3.plot(x,v,marker='o',label='time-volt')
    ax1.legend()
    ax2.legend()
    ax3.legend()

if __name__ == "__main__":
    ax1 = None
    ax2 = None
    ax3 = None
    
    instr24.write('*rst')
    instr24.write(':sour:func volt')
    instr24.write(':sens:curr:prot 1')
    instr24.write(':sens:func "curr"')
    instr24.write(':aver:coun 1')
    instr24.write(':sour:del 0')
    

    filename = initial_csv_62()
    t_2400 = threading.Thread(target=pluse_2400_self)
    t_plot = threading.Thread(target=plot_24)
    t_2400.start()
    
    t_plot.start()