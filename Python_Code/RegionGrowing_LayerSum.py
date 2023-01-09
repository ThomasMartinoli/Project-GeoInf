# -*- coding: utf-8 -*-
"""
Algoritmo di Region Growing
nel quale si fa scorrere la matrice pixel by pixel nella ricerca dei vicini dei seeds 
si sommano poi seeds&vicini + layer_grow
si trasforma il risultato (matrice di 0,1,2) in una matrice di (0,1) così da valutare 
eventualmente se introdurre nuovi seeds
si ripete il processo fino a che il numero di seeds
non resta invariato

@author: thmar
"""
#l'idea è quella di utilizzare una somma di Layer 
#e non scorrere pixel per pixel

#RG_LS region growing layer sum

#------------------------------------------------------------------------------
# Importing the libraries
#------------------------------------------------------------------------------

from Function import *
import numpy as np

def RG_LS(Raster,sizeR,sizeC):
    
    seed_array=np.array([])
    iterazioni=np.array([])
    N=np.count_nonzero(Raster[0])
    
    Seed=Raster[0,:,:].copy()
    M=0
    k=0
    
    while N!=M:
        
        M=N
        Vicini=CercaVicini(Seed,sizeR,sizeC)
        
        Result=Vicini+Raster[1]
        
        ModifiedResult= np.floor(Result/2)
        
        Seed=ModifiedResult
        
        seed_array=np.append(seed_array,N)
        iterazioni=np.append(iterazioni,k)
        
        N=np.count_nonzero(ModifiedResult)
        
        k=k+1
        
        
        print(N,M,k)
        
    return Seed, seed_array, iterazioni