# -*- coding: utf-8 -*-
"""
File che contiene una serie di funzioni utili 
nell'implementazione della fase di Region Growing

@author: thmar
"""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


#------------------------------------------------------------------------------
# Crea griglie colorate a seconda del valore del pixel: 
# 0 (unburned, green)
# 1 (burned, red)
#------------------------------------------------------------------------------

def ColorGrid(data,sizeR,sizeC):

    # create discrete colormap
    cmap = colors.ListedColormap(['green', 'red','blue'])
    bounds = [0,0.5,1.5,2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(0.5, sizeR, 1));
    ax.set_yticks(np.arange(0.5, sizeC, 1));

    plt.show()
  
    
#------------------------------------------------------------------------------
# Cerca gli 8 vicini di un pixel, nel nostro caso il pixel in questione
# è un seed e andiamo a selezionare i suoi vicini
#------------------------------------------------------------------------------

#copy() necessario altrimenti python crea non una coppia ma un collegamento
#e se modifivco uno allora modifico pure l'altro se si tratta di array

def CercaVicini(Seed,sizeR,sizeC):
    
    MatriceVicini=Seed.copy()
   
    #set the seed's neighbours to 1 
    #row
    for j in range(sizeR): 
        #column
        for k in range(sizeC):
            
            #element inside the matrix
            if Seed[0,j,k]==1 and j>0 and j<sizeR-1 and k>0 and k<sizeC-1:
                
                MatriceVicini[0][j-1:j+2,k-1:k+2]=1               
            
            #first row without corners
            if Seed[0,j,k]==1 and j==0 and k>0 and k<sizeC-1:
                
                MatriceVicini[0][j:j+2,k-1:k+2]=1
                
            #last row without corners
            if Seed[0,j,k]==1 and j==sizeR-1 and k>0 and k<sizeC-1:
                
                MatriceVicini[0][j-1:j+1,k-1:k+2]=1
       
            #first column without corners
            if Seed[0,j,k]==1 and j>0 and j<sizeR-1 and k==0:           
          
                MatriceVicini[0][j-1:j+2,k:k+2]=1
           
            #last column without corners
            if Seed[0,j,k]==1 and j>0 and j<sizeR-1 and k==sizeC-1:
          
                MatriceVicini[0][j-1:j+2,k-1:k+1]=1
              
            #upper-left corner
            if Seed[0,j,k]==1 and j==0 and k==0:            
               
                MatriceVicini[0][j:j+2,k:k+2]=1
            
            #upper-right corner
            if Seed[0,j,k]==1 and j==0 and k==sizeC-1:      
                         
                MatriceVicini[0][j:j+2,k-1:k+1]=1               
            
            #lower-left corner
            if Seed[0,j,k]==1 and j==sizeR-1 and k==0:               

                MatriceVicini[0][j-1:j+1,k:k+2]=1
            
            #lower-right corner
            if Seed[0,j,k]==1 and j==sizeR-1 and k==sizeC-1:
    
                MatriceVicini[0][j-1:j+1,k-1:k+2]=1
          
    return MatriceVicini
          
#------------------------------------------------------------------------------
# Index aggregation 
#------------------------------------------------------------------------------
# utilizzando l'articolo "bwimage"
# https://drive.google.com/file/d/1QB1sTlm3h1kzV8QThWVCWc99tosLjNPw/view

# l'idea,guardando i 4 vicini (a croce) di un pixel, è quella di assegnare a 
# ciascun pixel un valore pari a:
# 1 se 4 vicini su 4 hanno lo stesso valore del pixel 
# 0.75 se 3 vicini su 4 hanno lo stesso valore del pixel<
# 0.5 se 2 vicini su 4 hanno lo stesso valore del pixel
# 0.25 se 1 vicini su 4 hanno lo stesso valore del pixel
# 0 se 0 vicini su 4 hanno lo stesso valore del pixel
# inoltre non si considerano i bordi: prima ed ultima riga, prima ed ultima colonna
# indici j=0,k=0,j=size-1,k=size-1

import numpy as np
def AggregationIndex(SEED,size):
    AggregationMatrix=np.zeros([size-2,size-2])
    for j in range (size):
        for k in range (size):
    
            if j!=0 and k!=0 and j!=size-1 and k!=size-1:
                vicini=[SEED[j,k-1],SEED[j-1,k],SEED[j,k+1], SEED[j+1,k]]
                ones=np.count_nonzero(vicini)
                zeros=len(vicini)-ones
                if SEED[j,k]==0:
                    AggregationMatrix[j-1,k-1]=zeros/len(vicini)
                if SEED[j,k]==1:
                    AggregationMatrix[j-1,k-1]=ones/len(vicini)
                    
    # Number Of Rows
    Row=len(AggregationMatrix) 
    # Number Of Columns
    Column=len(AggregationMatrix)
    #Number Of Elements
    Elements= Row*Column  
    #Aggregation index, it is a mean           
    Index= sum(sum(AggregationMatrix))/Elements
    return Index,AggregationMatrix

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



