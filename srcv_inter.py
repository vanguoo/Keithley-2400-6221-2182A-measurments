from SRC_V import Ui_srcv
from PyQt5.Qt import *
from plot import *
from SourceV_MeasureI import *

class window(QWidget,Ui_srcv):
    #初始化一个存放 参数的数组 长度为9
    args = [None for _ in range(9)]
    emit_confirm = pyqtSignal()
    emit_start =  pyqtSignal()
    emit_stop = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('source v measure i')
        self.setupUi(self)

    @pyqtSlot()
    def on_start_clicked(self):
        
        self.emit_start.emit()
    
    @pyqtSlot()
    def on_confirm_clicked(self):
        
        
        self.start.setEnabled(True)
        self.emit_confirm.emit()
        # print(self.args)

    
    @pyqtSlot()
    def on_stop_clicked(self):
        
        self.emit_stop.emit()

    @pyqtSlot()
    def on_high_editingFinished(self):
        self.args[2] = self.high.text()
        print(self.args)

    @pyqtSlot()
    def on_low_editingFinished(self):
        self.args[3] = self.low.text()
        print(self.args)

    @pyqtSlot()
    def on_width_editingFinished(self):
        self.args[4] = self.width.text()
        print(self.args)
    
    @pyqtSlot()
    def on_compliance_editingFinished(self):
        self.args[5] = self.compliance.text()
        print(self.args)
    
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
    
    
    
    
    
def test():
    initial_csv_62(window.args[0],window.args[1])
    pluse_2400_self(window.args[2],window.args[3],window.args[4],window.args[5],window.args[6],window.args[7])
    

def start():
    go()

def stop():

    thread_kill()
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = window()
    
    win.emit_confirm.connect(test)
    win.emit_start.connect(start)
    win.emit_stop.connect(stop)
    
    win.show()
    sys.exit(app.exec_())