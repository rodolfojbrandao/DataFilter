import os
import pandas as pd
from multiprocessing import Pool
#import numpy as np

N = 4   #number of cores
a = list(range(N))
NF = 601

path = '/home/lablinux/simulacoes/esferas_porc/1-4/04/post_ParaviewPP'
os.chdir(path)
result = 0

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    filenumber = 0
    for j in range(0,NF):
        data = pd.read_csv('PP.{}.csv'.format(filenumber))
        velocity1 = data.iloc[:,0:3]
        velocity1.to_csv('velocity1.{}.csv'.format(filenumber))
        velocity2 = data.iloc[:,3:6]
        velocity2.to_csv('velocity2.{}.csv'.format(filenumber))
        force = data.iloc[:,8:11]
        force.to_csv('force.{}.csv'.format(filenumber))
        filenumber = filenumber + 1


#Data Paralellism = distributing the input data across processes
if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)