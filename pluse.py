from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import time

class pdelta():
    def __init__(self):
        self.setup()
        # self.test()

    def ok(self):
        print('ok')

    def test(self):
        rm = visa.ResourceManager('@py')
        instr1 = rm.open_resource('GPIB0::7::INSTR')

        instr1.query('*idn?')

        print(instr1.query('sour:pdel:nvpr?'))
        
        # time.sleep(3)
        # instr1.write('syst:comm:ser:send "volt:rang 1"')
        # temp1 = instr1.query('syst:comm:ser:send "volt:rang?"')
        # temp2 = instr1.query('syst:comm:ser:ent?')
        # time.sleep(2)
        # print(temp1)
        # print(temp2)

    def setup(self):
        rm = visa.ResourceManager('@py')
        instr1 = rm.open_resource('GPIB0::7::INSTR')

        instr1.write('*rst')
        instr1.write('unit voltage')
        
        instr1.write('sour:pdel:high 1e-3')
        instr1.write('sour:pdel:low 0')
        instr1.write('sour:pdel:width 100e-6')
        instr1.write('sour:pdel:sdel 10e-6')
        instr1.write('sour:pdel:count 200')
        instr1.write('sour:pdel:rang best')
        instr1.write('sour:pdel:int 10')
        
        instr1.write('sour:pdel:swe:off')

        instr1.write('sour:pdel:arm')
        instr1.write('init:imm')
        time.sleep(3)
        i=10
        flag= True
        while i:
            time.sleep(1)
            temp = instr1.query('sens:data?')
            print(temp)
            # print(instr1.query('sens:data:fres?'))
            # print(instr1.query(':trac:data?'))

            i -= 1

        instr1.write('sour:swe:abor')

if __name__ == "__main__":
    a = pdelta()
    