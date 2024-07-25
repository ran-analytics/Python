# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:27:01 2022

@author: sys-user
"""

import pandas as pd
import glob
import string
dirfile = open('D:\Golden copies\dirfile.txt', "r")
lines = []
for line in dirfile:
    lines.append(line)
dirfile.close()
inpdir = lines[0].rstrip('\n')
opdir =  lines[1].rstrip('\n')
fcnt=0
fn=glob.glob(inpdir+'/*.xlsx*')
for file in glob.glob(inpdir+'/*.xlsx'):
    fcnt+=1

def jf(e):
   # parstr = open(fn[e], 'r', encoding='utf8')
    df = pd.read_excel(fn[e])
    #print (df)
    of = fn[e].replace ('Input','Output').replace ('.xlsx','.parquet')
    df.to_parquet(of) #, encoding='utf8'
    print('The Parquet file is generated {}'.format(of))
    print("The process has been completed")

if __name__ == '__main__':
    #print("yes,main")
    print("Total number of excel files converted to parquet = {}".format(len(fn)))
    for i in range(0,fcnt):
        jf(i)