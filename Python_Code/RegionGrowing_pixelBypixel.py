# -*- coding: utf-8 -*-
"""
Algoritmo di Region Growing
nel quale si fa scorrere la matrice pixel by pixel nella ricerca di seed
si valuta poi se ci sono dei vicini da inserire (osservando l'OWAgrow, che deve essere maggiore di 0)
se l'esito è positivo questi vengono inseriti nel layer dei seed
e si continua a scorrere la matrice fino a che il numero di seeds non varia tra due iterazioni

con iterazione si intende far scorrere tutti gli elementi di una matrice

@author: thmar
"""

from Function import *
import numpy as np

def RG_PP(Raster,sizeR,sizeC):
    
    RasterPP=Raster.copy()
    iterazione=1
    M=0
    N=np.count_nonzero(RasterPP[0])
    
    seed_array=np.array([])
    step=np.array([])
    
    while N!=M:
        
        print(N,M,iterazione-1)
        M=N
        for j in range(sizeR):
            for k in range(sizeC):
                
                #insertion of the neighbors that are not considered yet
                
                if RasterPP[0][0,j,k]==1:
                    
                    if RasterPP[2][j,k]==-1:
                       RasterPP[2][j,k]=iterazione 
                    
                    # neighbor examination                
                    
                    # above-left   
                    if j>0 and k>0 and RasterPP[0][0,j-1,k-1]==0 and RasterPP[1][0,j-1,k-1]==1 and RasterPP[2][j-1,k-1]==-1:
                        RasterPP[0][0,j-1,k-1]=1
                        RasterPP[2][j-1,k-1]=iterazione
                    
                    # above
                    if j>0 and RasterPP[0][0,j-1,k]==0 and RasterPP[1][0,j-1,k]==1 and RasterPP[2][j-1,k]==-1:
                        RasterPP[0][0,j-1,k]=1
                        RasterPP[2][j-1,k]=iterazione
                    
                    #above-right
                    if j>0 and k<=sizeC-2 and RasterPP[0][0,j-1,k+1]==0 and RasterPP[1][0,j-1,k+1]==1 and RasterPP[2][j-1,k+1]==-1:
                        RasterPP[0][0,j-1,k+1]=1
                        RasterPP[2][j-1,k+1]=iterazione
                        
                    #left
                    if k>0 and RasterPP[0][0,j,k-1]==0 and RasterPP[1][0,j,k-1]==1 and RasterPP[2][j,k-1]==-1:
                        RasterPP[0][0,j,k-1]=1
                        RasterPP[2][j,k-1]=iterazione
                        
                    #right
                    if k<=sizeC-2 and RasterPP[0][0,j,k+1]==0 and RasterPP[1][0,j,k+1]==1 and RasterPP[2][j,k+1]==-1:
                        RasterPP[0][0,j,k+1]=1
                        RasterPP[2][j,k+1]=iterazione
                    
                    #below-left    
                    if j<=sizeR-2 and k>0 and RasterPP[0][0,j+1,k-1]==0 and RasterPP[1][0,j+1,k-1]==1 and RasterPP[2][j+1,k-1]==-1:
                        RasterPP[0][0,j+1,k-1]=1
                        RasterPP[2][j+1,k-1]=iterazione
                    
                    #below    
                    if j<=sizeR-2 and RasterPP[0][0,j+1,k]==0 and RasterPP[1][0,j+1,k]==1 and RasterPP[2][j+1,k]==-1:
                        RasterPP[0][0,j+1,k]=1
                        RasterPP[2][j+1,k]=iterazione
                    
                    #below-right    
                    if j<=sizeR-2 and k<=sizeC-2 and RasterPP[0][0,j+1,k+1]==0 and RasterPP[1][0,j+1,k+1]==1 and RasterPP[2][j+1,k+1]==-1:
                        RasterPP[0][0,j+1,k+1]=1
                        RasterPP[2][j+1,k+1]=iterazione                            
                         
        step=np.append(step,iterazione-1)                         
        iterazione=iterazione+1
        
        #condition that blocks the while
        seed_array=np.append(seed_array,N)
        N=np.count_nonzero(RasterPP[0])   
        
    return RasterPP, seed_array, step
