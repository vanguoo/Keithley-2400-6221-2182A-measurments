import visa
from gpib_ctypes import make_default_gpib
make_default_gpib()
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import threading
import time
import csv
import pandas as pd


rm = visa.ResourceManager('@py')
instr62 = rm.open_resource('GPIB0::7::INSTR')
instr21 = rm.open_resource('GPIB0::10::INSTR')

def file_init():
    feildname = ['current','resistance','time','resistance_low']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    temp = time.ctime().replace(' ','_')
    filename6 = temp.replace(':','_')
    filename6 = '{}/{}.csv'.format(directory,filename6)
    with open('%s' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6

def ok(amp_hig=5e-9,amp_low=0):
    instr62.write('cle')
    instr62.write('curr:rang:auto on')
    # instr62.write('curr:compliance 10')

    instr21.write('*rst')
    instr21.write(':sens:func "volt"')
    # instr21.write(':sens:volt:dc:rang 10')
    instr21.write(':sens:volt:dc:nplc 5')
    instr21.write(':trig:coun 1')

    k = 10
    while k:
        i=18
        loop_time_start1 = time.perf_counter()
        while i:
            start = time.perf_counter()
            instr62.write('curr %s' % amp_hig)
            instr62.write('outp on')
            volt1 = instr21.query('read?')

            resistance = str(float(volt1)/float(amp_hig))
            amp_hig = str(amp_hig)
            t = str(time.time())
            data =amp_hig,resistance,t
            data1 = ('%s\n' % (','.join(data)))
            print(data1)

            with open('%s' % filename,'a') as file1:
                file1.write(data1)

            i -=1
            stop = time.perf_counter()
            print(f'high time is {(stop-start)}')
        loop_time_stop1 = time.perf_counter()
        print(f'loop time is {(loop_time_stop1-loop_time_start1)}')
            
        j =18
        loop_time_start = time.perf_counter()
        while j:
            start1 = time.perf_counter()
            instr62.write('curr %s' % amp_low)
            instr62.write('outp on')
            instr21.write('init')
            volt2 = instr21.query('fetch?')
            # resistance1 = (str(float(volt2)/0.000000000111))

            t1 = str(time.time())
            
            data1 = str(0),str(0),t1
            data4 = ('%s\n' % (','.join(data1)))
            
            print(data4)
            with open('%s' % filename,'a') as file3:
                file3.write(data4)

            j-=1
            stop1 = time.perf_counter()
            print(f'low  time is {(stop1-start1)}')
        loop_time_stop = time.perf_counter()
        print(f'loop time is {(loop_time_stop-loop_time_start)}')
        k-=1
        print(k)
    instr62.write('outp off')

def plot_24():
    global ax1
    global ax2
    global ax3
    
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    ani = FuncAnimation(fig,animate,interval=10)
    plt.show()

def animate(i):
    data = pd.read_csv('%s' % filename)
    x = data['time']
    c = data['current']
    r = data['resistance']

    ax1.cla()
    ax2.cla()
    
    ax1.plot(x,c,marker='o',label='time-current',color='b')
    ax2.plot(x,r,marker='*',label='time-resistance',color='r')

    ax1.legend()
    ax2.legend()


if __name__ == "__main__":
    data_low = None
    data_hig = None

    ax1 = None
    ax2 = None
    ax3 = None

    filename = file_init()
    t1 = threading.Thread(target=ok)
    t2 = threading.Thread(target=plot_24)

    t1.start()
    t2.start()