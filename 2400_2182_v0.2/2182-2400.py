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
    feildname = ['time','current','res']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    # temp = time.ctime().replace(' ','_')
    # filename6 = temp.replace(':','_')
    filename6 = '{}.csv'.format(directory)
    with open('%s' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6

#2400模拟脉冲
def sour_basic():
    global high_val
    global low_val
    
    global flag
    global flag1
    global flag3
    high_val = 10e-9
    low_val = 0
    k=10
    instr24.write(':outp on')
    while k:
        i = 20
        while i:
            flag3 = False
            start = time.perf_counter()
            instr24.write(':sour:curr:lev %s' % high_val )
            instr24.write('init')
            flag3 = True
            flag = True
            stop = time.perf_counter()
            # print(f'high time is {(stop-start)}')
            i -=1
        
        j = 20
        while j:
            flag3 = False
            start1 = time.perf_counter()
            instr24.write(':sour:curr:lev %s' % low_val)
            instr24.write('init')
            flag3 = True
            flag = False
            stop1 = time.perf_counter()
            # print(f'low  time is {(stop1-start1)}')
            j -=1
        k -=1
        print(k)
    instr24.write('outp off')
    flag1 = False


def mes_2182():
    global a
    global flag2
    global t
    t = 0
    
    while flag1:
        # if flag3 ==True:
        start = time.perf_counter()
        a = instr21.query('read?')
        flag2 = True
        stop = time.perf_counter()
        print(f'mes time is {(stop-start)}')

        t += stop-start
        


def data_anlysis():
    while flag1:
        
        if flag == True:
            
            if flag2 == True:
                res = float(a)/high_val
                res = str(res)
                t1 = round(t,3)
                data = str(t1),str(high_val),res,'\n'
                print(data)
                data = ','.join(data)
                time.sleep(0.05)
                
                with open('%s' % filename,'a') as file3:
                    file3.write(data)
            elif flag2 == False:
                print('wait..')
                

        elif flag == False:
            print('0')
            if flag2 ==True:
                t1 = round(t,3)
                data1 = str(t1),str(low_val),str(0),'\n'
                data1 = ','.join(data1)
                time.sleep(0.05)
                
                with open('%s' % filename,'a') as file3:
                        file3.write(data1)
            elif flag2 == False:
                print('wait..')

    


    
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
    high_val = None
    low_val = None
    a = None
    t = None
    ax1 = None
    ax2 = None
    ax3 = None
    flag = False
    flag1 = True
    flag2 = False
    flag3 = None

    instr21.write('*rst')
    instr21.write(':sens:func "volt"')
    instr21.write(':sens:volt:dc:rang 10')
    instr21.write(':sens:volt:dc:nplc 1')
    instr21.write(':trig:coun 1')

    instr24.write('*rst')
    instr24.write(':sour:func curr')
    

    filename = file_init()

    t_plot = threading.Thread(target=plot_24)
    t_data = threading.Thread(target=data_anlysis)
    t_2182 = threading.Thread(target=mes_2182)
    t_src = threading.Thread(target=sour_basic)
 
    t_src.start()
    t_plot.start()
    t_2182.start()
    t_data.start()

