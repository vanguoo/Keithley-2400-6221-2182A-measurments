import visa
from gpib_ctypes import make_default_gpib
make_default_gpib()
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import threading
import time
import csv
import pandas as pd

rm = visa.ResourceManager()
print(rm.list_resources())
instr21 = rm.open_resource('ASRL4::INSTR')
instr62 = rm.open_resource('ASRL5::INSTR')

# print(instr21.query('*Idn?'))
# print(instr62.query('*Idn?'))



