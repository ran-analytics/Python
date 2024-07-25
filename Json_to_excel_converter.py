from copy import deepcopy
import json
import pandas as pd
import os
import glob

dirfile = open('dirfile.txt', "r")
lines = []
for line in dirfile:
    lines.append(line)
dirfile.close()
inpdir = lines[0].rstrip('\n')
opdir =  lines[1].rstrip('\n')
fcnt=0
fn=glob.glob(inpdir+'/*.json')
for file in glob.glob(inpdir+'/*.json'):
    fcnt+=1
def cross_join(left, right):
    new_rows = []
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem) # intermediate result to the caller.can run multiple times.
        else:
            yield elem #This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory. 
#Yield is used in Python generators. A generator function is defined just like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 

def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows


    return pd.DataFrame(flatten_json(data_in))

def jf(e):
    jsonStr = open(fn[e], 'r', encoding='utf8')
    json_data = json.load(jsonStr)
    #print("length of json_data is:" ,len(json_data))
    df = json_to_dataframe(json_data)
    of = fn[e].replace ('Input','Output').replace ('.json','.xlsx')
    df.to_excel(of, encoding='utf8')
    print('The Json data has been written to: {}'.format(of))
    print("The process has been completed")
    jsonStr.close

if __name__ == '__main__':
    print("Total number of excel files converted to json = {}".format(len(fn)))
    for i in range(0,fcnt):
        jf(i)
