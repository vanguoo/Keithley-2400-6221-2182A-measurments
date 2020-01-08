import csv
import time 
from random import randint


# here we are going to generate random number

def init_csv():
    fieldname = ['time','value1','value2']
    temp = time.ctime().replace(' ','_')
    filename = temp.replace(':','_')
    directory = '2400'
    filename = "{}/{}".format(directory,filename)
     
    with open('%s' % filename,'w') as file1:
        writer = csv.DictWriter(file1,fieldnames=fieldname)
        writer.writeheader()
    return filename

def num_gen(file_num):
    i = 20
    value1 = 100
    value2 = 50
    t = 0 
    while i:
        
        value1 += randint(0,10)
        value2 += randint(0,10)

        data = '{},{},{}\n'.format(t,value1,value2)
        with open(file_num,'a') as file2:
            file2.write(data)
        i -=1
        t +=1
        time.sleep(1)


if __name__ == "__main__":
    filename1 = init_csv()
    num_gen(filename1)