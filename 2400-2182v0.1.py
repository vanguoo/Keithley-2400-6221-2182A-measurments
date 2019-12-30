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
instr24 = rm.open_resource('GPIB0::24::INSTR')
instr21 = rm.open_resource('GPIB0::10::INSTR')

#初始化csv文件
def file_init():
    feildname = ['voltage','current','res','time','resistance','real_res']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    # temp = time.ctime().replace(' ','_')
    # filename6 = temp.replace(':','_')
    filename6 = '{}.csv'.format(directory)
    with open('%s' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6

#2400模拟脉冲
def sour_basic(high_val=-3e-9,low_val=0.0000000000000):
    
    
    k=20
    temp = 0
    temp1 = 0
    while k:
        

        j = temp1 + 15

        while j:
            start1 = time.perf_counter()
            instr24.write(':sour:curr:lev %s' % low_val)
            instr24.write('init')
            instr21.write('init')
            data1 = instr24.query('fetch?').split(',')
            volt_1 = instr21.query('fetch?')

            data1.pop()
            res = str(float(volt_1)/float(data1[1]))
            data1.append('%s' % str(0) )
            data1.append('%s\n' % str(res))
            # data1.append('%s\n' % str(volt_1))
            data_low = ','.join(data1)
       
            with open('%s' % filename,'a') as f2:
                f2.write(data_low)

            stop1 = time.perf_counter()
            print(f'low  time is {(stop1-start1)}')
            j -=1
        temp1 +=15

        i = temp + 15
        while i:
            start = time.perf_counter()
            instr24.write(':sour:curr:lev %s' % high_val )
            instr24.write('init')
            instr21.write('init')
            data = instr24.query('fetch?').split(',')
            volt21 = instr21.query('fetch?')

            data.pop()
            res = str(float(volt21)/float(data[1]))
            data.append('%s'%res)
            data.append('%s\n'%res)
            # data.append('%s' % volt21)
            data_hig = ','.join(data)
            with open('%s' % filename,'a') as f1:
                f1.write(data_hig)
            stop = time.perf_counter()
            print(f'high time is {(stop-start)}')
            i -=1
        temp += 15
        
        print(i)
        
        k -=1
        print(k)
    instr24.write('outp off')
    
#画图模块
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

    instr21.write('*rst')
    instr21.write(':sens:func "volt"')
    # instr21.write(':sens:volt:chan2:ref:stat off')
    # instr21.write(':sens:volt:ref 10')
    # instr21.write(':sens:volt:ref:acq')
    # instr21.write(':sens:volt:ref:stat on')
    instr21.write(':sens:chan 1')

    instr21.write(':sens:volt:dc:nplc 1')
    instr21.write(':trig:coun 1')

    instr24.write('*rst')
    instr24.write(':sour:func curr')
    # instr24.write(':sens:func "volt"')
    instr24.write(':outp on')

    filename = file_init()

    t_plot = threading.Thread(target=plot_24)
    t_mes = threading.Thread(target=sour_basic)
 
    t_mes.start()
    t_plot.start()