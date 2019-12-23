import pluse
import swe
import threading
import p_live


def option():
    print('*****           welcome!        *****')
    print('***** please enter your command *****')
    print('*****   "2400" for sweep mode   *****')
    print('*****   "6221" for pluse mode   *****\n')
    op1 = input(' ')
    flag=True
    while (flag):
        if op1=='2400':
            print('2400 initialing...')
            
            swe_2400()
            flag=False
        if op1=='6221':
            print('6221 initialing...')
            pul_6221()
            flag=False
        else: flag=False
    print('done!')

def pul_6221():
    a = pluse.pdelta()
    a.setup()

def swe_2400():
    start = swe.mes()
    start.init_csv()
    start.sweep_mode()
    plot_thread = threading.Thread(target=plot, name='make_plot')
    plot_thread.start()
    
    
def plot():
    p_live.liveplot_2400()
    

if __name__ == "__main__":
    option()