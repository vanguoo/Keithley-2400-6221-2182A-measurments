from MainUi import Ui_Form
import SRC_V
import SRC_I
from PyQt5.Qt import *

class Window(QWidget,Ui_Form):
    
    show_srci_signal = pyqtSignal()
    show_srcv_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('2400PulseMode')
        self.setupUi(self)

    @pyqtSlot()
    def on_SRC_I_clicked(self):
        print('jump it ')
        self.uiv = SRC_I.Ui_Dialog()
        self.setupUi(self)
        self.uiv.show()
    
    @pyqtSlot()
    def on_SRC_V_clicked(self):
        print('jump src v')
        self.uii = SRC_V.Ui_Dialog()
        self.setupUi(self)
        self.uii.show()
        # self.show_srcv_signal.emit()

    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Window()

    # def show_srcv():
    #     uiv = SRC_V.Ui_Dialog()
    #     uiv.show()
    
    # def show_srci():
    #     print('ok')

    # win.show_srci_signal.connect(show_srci)
    # win.show_srcv_signal.connect(show_srcv)
    win.show()
    
    sys.exit(app.exec_())