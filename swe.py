from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import csv
import time
import threading


class mes():

    def init_csv(self):
        fieldname = ['value1','value2','value3','TimeStamp','resistance']
        self.filename=input('you want data save as:')
        with open('%s.csv' % self.filename,'w') as file:
            write_header = csv.DictWriter(file,fieldnames=fieldname)
            write_header.writeheader()
        return self.filename

    def sweep_mode(self):
        print('***start**stop**step**cmpliance***')
        a,b,c,d,cmpl= map(float,input(' ').split(','))
        
        rm = visa.ResourceManager('@py')
        instr = rm.open_resource('GPIB0::24::INSTR')
        instr.write('*rst')
        instr.write(':outp on')
        instr.write(':sour:func volt')
        instr.write(':sens:curr:prot %s' % cmpl)
        instr.write(':sens:func "curr:dc"')
        # self.write(':sens:func "res"')
        i = a
        flag = True
        while (flag):
            instr.write(':sour:volt:lev %f' % i)
            instr.write(':read?')
            time.sleep(1)
            data = instr.read()

            list_data = data.split(',')
            list_data.pop()
            resistance = float(list_data[0])/float(list_data[1])
            list_data.append('%s\n' % resistance)
            data1 = ','.join(list_data)
            print(data1)

            with open('%s.csv' % self.filename, 'a') as file:
                file.write(data1)
            i += c
            x = round(i, 2)

            if x == b:
                flag = False
                instr.write(':outp off')
                print('done!')


    


















