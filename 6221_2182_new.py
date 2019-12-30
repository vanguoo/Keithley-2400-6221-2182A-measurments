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

rm = visa.ResourceManager()
instr21 = rm.open_resource('ASRL4::INSTR')
instr62 = rm.open_resource('ASRL5::INSTR')

def file_init():
    feildname = ['time','res']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    # temp = time.ctime().replace(' ','_')
    # filename6 = temp.replace(':','_')
    filename6 = '{}.csv'.format(directory)
    with open('%s' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6


    

def src_6221():
    global curr
    global flag
    global flag1
    
    curr = 3e-9
    k = 20
    while k:
        
        j = 100
        while j:
            flag = False
            instr62.write('curr %s' % 0.000000) #10ms
            
            j -=1

        i = 100
        while i:
            flag = True
            instr62.write('curr %s' % curr)  #10ms
            
            i -=1

        k -=1
        print(k)
    flag1 = False
    


def mes_2182():
    global a
    global flag2
    global t
    t = 0
    
    while flag1:
        
        start = time.perf_counter()
        a = instr21.query('read?')
        flag2 = True
        t +=0.08
        stop = time.perf_counter()
        # print(f'measure time is {stop-start}')



def data_anly():

    while flag1:
        
        if flag == True:
                # print('1')
            if flag2 == True:
                res = float(a)/curr
                res = str(res)
                t1 = round(t,3)
                data = str(t1),res,'\n'
                data = ','.join(data)
                time.sleep(0.05)
                
                with open('%s' % filename,'a') as file3:
                    file3.write(data)
            elif flag2 == False:
                print('wait..')
                

        elif flag == False:
                # print('0')
            if flag2 ==True:
                t1 = round(t,3)
                data1 = str(t1),str(0),'\n'
                data1 = ','.join(data1)
                time.sleep(0.05)
                
                with open('%s' % filename,'a') as file3:
                        file3.write(data1)
            elif flag2 == False:
                print('wait..')
       
            

def plot():
    global ax1
    global filename
    
    print(filename)
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ani = FuncAnimation(fig,animate,interval=1)
    plt.show()
    

def animate(i):
    
    data2 = pd.read_csv('%s' % filename)
    t2 = data2['time']
    res1 = data2['res']
    

    ax1.cla()

    ax1.plot(t2,marker='o',label='time-res',c='b')

    ax1.legend()
    

if __name__ == "__main__":
    curr = None
    a = None
    t = None

    ax1 = None
    
    flag = False
    flag1 = True
    flag2 = False
    
    filename = file_init()

    instr21.write('*rst')
    instr21.write(':sens:func "volt"')
    instr21.write(':sens:volt:dc:rang 10')
    instr21.write(':sens:volt:dc:nplc 1')
    instr21.write(':trig:coun 1')

    instr62.write('cle')
    instr62.write('curr:rang:auto on')
    instr62.write('outp on')

    t_2182 = threading.Thread(target=mes_2182)
    t_6221 = threading.Thread(target=src_6221)
    t_plot = threading.Thread(target=plot)
    t_data = threading.Thread(target=data_anly)

    t_6221.start()
    t_2182.start()
    t_plot.start()
    t_data.start()
    
    t_2182.join()
    t_6221.join()
    t_data.join()
    t_plot.join()
    
    print('done!')
    
    
    