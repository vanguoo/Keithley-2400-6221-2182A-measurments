# import pluse
# import swe
import threading
import os
import csv
import time
from decimal import Decimal
from queue import Queue


def option(): 
    
    print('\n\n**                    Welcome!                 **')
    print('*************************************************')
    print('==         2400 Mode           6221 Mode       ==')
    print('==      Src V & Mes I        Pls I & Mes R     ==')
    print('*************************************************')
    print('==                   2400 Mode                 ==')
    print('*************************************************')
    # print('                  Sub Menu\n             "1" -> [Data Storage]\n             "2" -> [Sweep Sequence]\n             "3" -> [Start Sweep]\n             "4" -> [Help] \n')
    print('*************************************************')
    print('==                   6221 Mode                 ==')
    print('*************************************************')
    # print('                  Sub Menu\n             "1" -> [Data Storage]\n             "2" -> [Pluse Configure]\n             "3" -> [start pluse] \n')
    print('*************************************************')
    print('*****                  :-)                  *****')
    print('*************************************************')
    global filename
    global filename_62
    global dict1
    global dict2
    flag=True
    flag1=True
 
    while (flag):
        flag=True
        print('\n=======    [main menu] enter you command:   ======')
        print('====  "24" for 2400 Mode  "62" for 6221 Mode   ===')
        op1 = input(' ')

        if op1=='24':
            flag1=True
            while (flag1):
                print('=======   [sub menu 24] enter you command:  ======')
                print('====            "1"--> [data storage]         ==== ')
                print('====            "2"--> [sweep sequence]       ==== ')
                print('====            "3"--> [start sweeep]         ==== ')
                print('====            "4"--> [help]                 ==== ')
                cmd1 = input('')
                
                #data storage
                if cmd1=='1':
                    while 1:
                        print('====       Here is [data storage] menu         ===')
                        print('====     "m" to make a new directory           ===')
                        print('====        "a" for auto saving                ===')
                        cmd2 = input('')
                        if cmd2=='m':
                            data_storage()
                        
                        elif cmd2=='a':
                            filename = auto_saving()
                            print(filename)

                        elif cmd2=='q':
                            break
                        
                # sweep sequence
                if cmd1=='2': 
                    
                        print('===         Here is [sweep sequence] menu      ===')
                        data1 = set_sweep_seqence()
                        dict1 = dict_memory(data1)
                        print(dict1)
                
                #start sweep
                if cmd1=='3':   
                    sweep_multi()
                    sweep_done()

                #help
                if cmd1=='4':   
                    print('arange here ')
                    flag1=False 
                
                if cmd1=='q': 

                    flag1=False          
      
        if op1=='62':
            
            while 1:
                print('=======    [sub menu 62] enter you command:  ======')
                print('====            "1"--> [data storage]         ==== ')
                print('====            "2"--> [pluse setting]       ==== ')
                print('====            "3"--> [start pluse ]         ==== ')
                print('====            "4"--> [help]                 ==== ')
                op_62 = input('')
                if op_62 == '1':
                    print('====       Here is [data storage] menu         ===')
                    print('====     "-mkdir" to make a new directory      ===')
                    print('====            "a" for auto-saving            ===')
                    sub1 = input('')
                    if sub1 =='-mkdir':
                        data_storage()
                    elif sub1 == 'a':
                        filename_62 = initial_csv_62()
                        print('your file is %s' %filename_62)
                    elif sub1 =='q':
                        break

                #pluse configuring
                if op_62 =='2':
                    print('===         Here is [pluse config] menu      ===')

                    dict2= pluse_config()
                    
                       
                #pluse start
                if op_62 =='3':
                    pluse_multi()
                    

                if op_62 =='q':
                    break

        elif op1=='q':
            flag=False

    print('done!')


def initial_csv_62():
    feildname = ['resistance','time']
    directory = input('****please input your directory: ***\n*****please make sure the directory does exists\n')
    temp = time.ctime().replace(' ','_')
    filename6 = temp.replace(':','_')
    filename6 = '{}/{}.csv'.format(directory,filename6)

    with open('%s.csv' % filename6,'w') as file2:
        csv_writer = csv.DictWriter(file2,fieldnames=feildname)
        csv_writer.writeheader()
    return filename6

def pluse_config():
    print('*******     attention!  ***********')
    print('**** high pluse value [-105mA ~ 105mA]')
    print('**** low pluse value [-105mA ~ 105mA] ')
    print('**** pluse width value [50e-6 ~ 12e-3] seconds ')
    print('**** source delay value [16e-6 ~ 11.996e-3] seconds ')
    print('**** pdelay-sdelay >= 34e-6   *****')
    print('**** press "q" to quit  ')
    count = 1
    dict2 = {}
    while 1:
        list_pluse = input('sequence_%s: please input [high_amp(A),low_amp(A),width(s),time(s)]:\n' % count).split(',')
        
        if 'q' in list_pluse:
            break
        elif len(list_pluse)<4 or len(list_pluse)>4:
            print('Oops! please 4 arguments needed,please input again\n')
            continue
        dict2['sequence_%s' % count] = list_pluse
        count +=1           
        # sdel = float(c-30e-6)
    return dict2

def pluse_multi():
    t3 = threading.Thread(target=plot_62)
    t4 = threading.Thread(target=pluse_trigger)
    t3.start()
    t4.start()
    t4.join()   


def pluse_trigger():
    print(dict2)
    temp = pluse.pdelta()
    count = 1
    while 1:
        a,b,c,d = dict2['sequence_%s' % count]
        e = Decimal(str(c))-Decimal(str(34e-6))

        e = str(e)
    
        # temp.setup(a,b,c,d,e)

        print(a,b,c,d,e)
        count +=1
        if count>len(dict2):
            break

    
def plot_62():
    
    plot62 = pluse.pdelta()
    plot62.live_plot(file_62=filename_62)





#2400 func
def auto_saving():
    fieldname = ['voltage','current','value3','TimeStamp','resistance']
    temp = time.ctime().replace(' ','_')
    filename = temp.replace(':','_')
    
    directory = input('*****  confirm your directory: *****\n*****  please ensure that the directory done exists  *****\n')

    filename = '{}/{}'.format(directory,filename)

    with open('{}.csv'.format(filename),'w') as file_auto:
    
        write_header = csv.DictWriter(file_auto,fieldnames=fieldname)
        write_header.writeheader()
    
    return filename


def data_storage():  #创建目录
    temp = input('input dir:')
    os.mkdir("%s" % temp )

def set_sweep_seqence():   #配置 测量数据
    print('====       press "q" to stop your setting      === ')
    count = 1
    
    para_list = []
    while 1:
        list_swe = input('sequence_%d: start,stop,step,cmpl:' % count).split(',')
        para_list.append(list_swe)
        if len(list_swe)==4:
            count +=1
        elif 'q' in list_swe:
            break
        else:
            print('Oops! please enter again')
    
    para_list.pop()
    return para_list

def dict_memory(*args):  #把配置数据存储在字典中 dict1
    count = 1
    dict1 = {}
    for i in args:
        for j in i:
            dict1['sequence_%s' % count] = j
            count +=1
    return dict1

def plot(): 
    flag_plot = True  
    test = swe.mes()
    test.live_plot(filename_para=filename)
 
def sweep_multi():   
    
    t1 = threading.Thread(target=plot)
    
    t2 = threading.Thread(target=trigger)
    t1.start()
    t2.start()
    t2.join()
    


def sweep_done():  #测量完成的选项
    while 1:
        print('****[y] for sweep again with previous sequence')
        print('****[m] for change your sweep sequence')
        print('****[q] for quit sweep mode ')
        swe_agin = input('****sweep again?****\n')
        if swe_agin == 'y':
            print('yes')
            trigger()     
        elif swe_agin =='m':
            dict1 = modify_dict()
        else:print('done!');break
            

def modify_dict():   #测量完成修改数据
    count1 = 1
    print('here is your sequence: :)')
    while 1:
        temp = dict1['sequence_%s' % count1]
        print('sequence_%s : %s ' % (count1,str(temp)))
        count1 +=1
        if count1>len(dict1):
            break
    count2=1
    while 1:
        x = input('\nchange your sequence_%s: start,stop,step,cmpl\n' % count2).split(',')
        if 'q' not in x: 
            dict1['sequence_%s' % count2] = x
            print(dict1['sequence_%s' % count2])      
        count2 +=1
        if count2>len(dict1):
            break
    return dict1

def trigger():     #开启2400正式测量
    sample = swe.mes()
    global flag_plot
    
    count = 1
    while 1:
        list1 = dict1['sequence_%s' % count]
        count +=1
        a=list1[0];b=list1[1];c=list1[2];cmpl=list1[3]
        time.sleep(1)
        print(a,b,c,cmpl)
        sample.sweep_mode(a,b,c,cmpl)
        if count>len(dict1):
            break

    print('done!')
    flag_plot = False
    
    
 
if __name__ == "__main__":
    filename = None
    filename_62 = None
    dict1 = None
    dict2 = None
    flag_plot = None
    option()