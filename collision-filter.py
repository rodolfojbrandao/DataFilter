import os
import numpy as np
import pandas as pd
from multiprocessing import Pool

N = 24 #number of cores
a = list(range(N))
NF = 4000
path='/home/rodolfo/Desktop/25/CSVs_gran'
os.chdir(path)
result = 0

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    for j in range(inicio,fim):
        filenumber = 18150 + 726 * j
        data = pd.read_csv('dumpgran{}.csv'.format(filenumber))
        data.drop(data.index[0:8], inplace=True)
        data.to_csv('dumpgran{}.csv'.format(filenumber))

if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)