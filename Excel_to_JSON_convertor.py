import json
import pandas as pd
import glob  #global - to search for filenames
import os
#import exceltojson
#inpdir= 'D:/Working item/exceltojson/'
dirfile = open('dirfile.txt', "r")
lines = []
for line in dirfile:
    lines.append(line)
    #print (line)
dirfile.close()
inpdir = lines[0].rstrip('\n')
opdir =  lines[1].rstrip('\n')
#fcnt=0
#print(inpdir)
fn = glob.glob(inpdir + '/*.xlsx')
#for file in glob.glob(inpdir+ '/*.xlsx'):
 #   fcnt+=1
def json_call(x):
        excel_data_df = pd.read_excel(fn[x])
        #print(fn[x])
        #print(len(excel_data_df)) - length will always be 1 for dataframe
        of = fn[x].replace ('Input','Output').replace ('.xlsx','.json')
        excel_data_df.to_json(of, orient='records')
        #print(excel_data_df.to_json(of))
        #json_file.close()
        print("The json file {} has been generated successfully and available in the path {}".format(of[:-5]+'.json',opdir))
if __name__ == '__main__':
    print("Total number of excel files converted to json = {}".format(len(fn)))
    #print (fn)
    for i in range(0, len(fn)):
        json_call(i)