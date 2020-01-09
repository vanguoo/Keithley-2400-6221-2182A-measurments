from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import time

rm = visa.ResourceManager("@py")
instr1 = rm.open_resource('GPIB0::7::INSTR')

instr1.write('*rst')
instr1.write('unit v')
instr1.write('SOUR:PDEL:HIGH 10e-9')
instr1.write('SOUR:PDEL:LOW 0')
instr1.write('SOUR:PDEL:WIDT 80e-6')
instr1.write('SOUR:PDEL:SDEL 55e-6')
instr1.write('SOUR:PDEL:COUN 1')
instr1.write('SOUR:PDEL:RANG BEST')
# instr1.write('SOUR:PDEL:INT 10')
# instr1.write('SOUR:PDEL:SWE OFF')
# instr1.write('SOUR:PDEL:LME 2')

# instr1.write('TRAC:POIN 200')
instr1.write('SOUR:PDEL:ARM')
instr1.write('INIT')

# print(instr1.query('sens:data?'))

time.sleep(1)
i = 20
while i:
    print(instr1.query('sens:data?'))
    i -=1