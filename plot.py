import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from sensor import*
import threading
import multiprocessing


filename = None
ax1 = None
t2 = None
t1 = None

def animate(i):
    data = pd.read_csv(filename)
    x = data['time']
    y = data['value1']
    z = data['value2']
    ax1.cla()
    ax1.plot(x,y,z,label='time-value1',marker='*')
    
    ax1.legend()

def plot(file):
    global ax1
    global filename
    filename = file
    plt.style.use("ggplot")
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ani = FuncAnimation(fig,animate,interval=1000,repeat=True)
    plt.show()

def go():
    global t2
    global t1
    filename = init_csv()
    t1 = multiprocessing.Process(target=num_gen,args=(filename,))
    t2 = multiprocessing.Process(target=plot,args=(filename,))
    t1.start()
    t2.start()

    
    # t1.join()
    # t2.join()

def thread_kill():

    t2.terminate()
    t1.terminate()

if __name__ == "__main__":
    
    go()
