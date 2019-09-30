import os
import numpy as np
import pandas as pd
from multiprocessing import Pool

N = 24 #number of cores
a = list(range(N))
NF = 490
path='/media/rodolfo/5A0819190818F5AB/Doutorado/numerico/CasosMisturados/07c/dados'
os.chdir(path)
result = 0

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    for j in range(inicio,fim):
            data = pd.read_csv('dados.{}.csv'.format(j))
            data = data.drop(['id', 'f:0', 'f:1', 'f:2', 'omega:0', 'omega:1', 'omega:2'], axis = 1)
            data.to_csv('dados.{}.csv'.format(j))

if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)