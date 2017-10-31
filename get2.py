#coding:utf-8
import sys
import csv
import os
import __main__
import openpyxl
from openpyxl.styles import Border,Side
import re

def logsget():
    logs = os.listdir('./logs')
    list2 = [(re.search("[0-9]+", x).group(), x) for x in logs]
    list2.sort(key=lambda x:(int(x[0])))
    #i = 0
    #while i < 21:
    ##    print("{0:03d}".format(int(list2[i][0])))
     #   i = i + 1
    #exit()
    logs = [x[1] for x in list2]
    ll = len(logs)
    __main__.ll = ll
    __main__.logs = logs

def getwrite():
    with open('data.csv','w',newline='') as f:
        csvWriter = csv.writer(f)
        i = 0
        while i < ll:   
            listdata =[]
            ld = open("./logs/"+logs[i],'r',encoding='UTF-8',errors='ignore')
            lines = ld.readlines()
            ld.close()
            for line in lines:
                if line.find("Temp: CPU (Degrees C)") >= 0:
                    a = line[:-1]
                elif line.find("Temp: System (Degrees C)") >= 0:
                    b = line[:-1]
                elif line.find("Hardware is VLAN, address is") >= 0:
                    c = line[:-1]
            a = a[45:47]
            b = b[45:47]
            c = c[31:45]
            listdata.extend([logs[i],"",a,b,"",c])
            csvWriter.writerow(listdata)
            i = i + 1

if __name__ == '__main__':
    logsget()
    getwrite()
    exit()

