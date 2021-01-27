#! /usr/bin/env python3

import pandas as pd 
import numpy as np
import sys
import os
import io

buf = io.StringIO()

file_path = sys.argv[1]
output_name = 'graphs'
# output_name = sys.argv[2]
# output_name = sys.argv[1]

# print(file_path)
#print(output_name)

print(sys.argv[0], sys.argv[1])



def quick_eda(file_path):
    df = pd.read_csv(file_path)
    info = df.info(buf=buf)
    info_print = buf.getvalue()
    describe = df.describe()
    null = df.isnull().sum()
    print('~~~~~info~~~~~')
    print(info_print)
    print('~~~~~~~NULL Values~~~~~~')
    print(null)
    for columns in describe:
        print(f'~~~~~~{columns}~~~~~~~')
        print(describe[columns])
    dtypes_dict = df.dtypes.to_dict()
    for column in dtypes_dict:
        if dtypes_dict[column] == np.dtype('float64')\
        or dtypes_dict[column] == np.dtype('int64'):
            ax = df[column].plot(kind='hist')
            ax.figure.savefig(f'./output_{output_name}/{column}.png')


quick_eda(file_path)
