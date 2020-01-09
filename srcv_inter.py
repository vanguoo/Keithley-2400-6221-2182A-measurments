from SRC_V import Ui_srcv
from PyQt5.Qt import *
from plot import *
from SourceV_MeasureI import *
from multiprocessing import Process
import visa

t_2400 = None
t_plot = None

class window(QWidget,Ui_srcv):
    #初始化一个存放 参数的数组 长度为9
    args = [None for _ in range(10)]
    emit_switching1 = pyqtSignal()
    emit_switching = pyqtSignal()
    emit_start =  pyqtSignal()
    emit_stop = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('source v measure i')
        self.setupUi(self)
        self.args[8] = "volt"
        self.args[9] = "curr"
        print('here is source volt mode')
        rm = visa.ResourceManager('@py')
        instr24 = rm.open_resource('GPIB0::24::INSTR')
        instr24.write('*rst')

    @pyqtSlot(bool)
    def on_radioButton_toggled(self,bool):
        if bool:
            # args[8] = src_func  args[9] = sens_func

            self.emit_switching.emit()
        else:
            
            self.emit_switching1.emit()


    
    # @pyqtSlot()
    # def on_radioButton_released(self):
    #     print('source i')

    @pyqtSlot()
    def on_start_clicked(self):
        
        self.emit_start.emit()
    
    @pyqtSlot()
    def on_stop_clicked(self):
        
        self.emit_stop.emit()

    @pyqtSlot()
    def on_high_editingFinished(self):
        self.args[2] = self.high.text()
        

    @pyqtSlot()
    def on_low_editingFinished(self):
        self.args[3] = self.low.text()
        

    @pyqtSlot()
    def on_width_editingFinished(self):
        self.args[4] = self.width.text()
        
    
    @pyqtSlot()
    def on_compliance_editingFinished(self):
        self.args[5] = self.compliance.text()
        
    
    @pyqtSlot()
    def on_dir_editingFinished(self):
        self.args[0] = self.dir.text()
    
    @pyqtSlot()
    def on_filename_editingFinished(self):
        self.args[1] = self.filename.text()
    
    @pyqtSlot()
    def on_period_editingFinished(self):
        
        self.args[6] = self.period.text()        
        
    @pyqtSlot()
    def on_rate_editingFinished(self):
        
        self.args[7] = self.rate.text()
    
def switching_srci():
    window.args[8] = "curr"
    window.args[9] = "volt"
    print('here is source current mode')

def switching_srcv():
    #defult is src_volt
    window.args[8] = "volt"
    window.args[9] = "curr"
    print('here is source voltage mode ')

def start():
    global t_2400
    global t_plot
    print('initializing...')
    filename1 = initial_csv_62(window.args[0],window.args[1])
    t_2400 = Process(target=pluse_2400_self,args=(window.args[8],window.args[9],filename1,window.args[2],window.args[3],window.args[4],window.args[5],window.args[6],window.args[7],))
    t_plot = Process(target=plot_24,args=(filename1,))
    t_2400.start()
    t_plot.start()
    
    # go()

def stop():
    t_2400.terminate()
    t_plot.terminate()
    stop_process()
    # thread_kill()
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = window()
    
    
    win.emit_start.connect(start)
    win.emit_stop.connect(stop)
    win.emit_switching.connect(switching_srci)
    win.emit_switching1.connect(switching_srcv)
    
    win.show()
    sys.exit(app.exec_())