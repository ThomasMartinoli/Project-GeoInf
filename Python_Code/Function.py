# -*- coding: utf-8 -*-
"""
This file contais the functions that are useful in order to run the Main

"""
#------------------------------------------------------------------------------
# Importing the libraries
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import rasterio
import os
import copy

#------------------------------------------------------------------------------
# Export the result in a .TIF
#------------------------------------------------------------------------------


def ExportResult(Burned,sizeR,sizeC):
    path = os.getcwd()
    
    Seed_file = "\\seed_binary.tif"
    SeedTif=rasterio.open(path+Seed_file)
        
        
    Seed_array = SeedTif.read()
    Result=copy.deepcopy(Seed_array[:,0:sizeR,0:sizeC])
    Result[0]=Burned
        
    Result_File="\Result.tif"
    Result_File_Out=path+Result_File
    
    with rasterio.open(Result_File_Out,
                       'w',                    
                       driver = SeedTif.meta['driver'],
                       height = sizeR,
                       width= sizeC,
                       count=SeedTif.meta['count'],
                       crs=SeedTif.meta['crs'],
                       transform=SeedTif.meta['transform'],
                       dtype= SeedTif.meta['dtype'],
                       nodata= SeedTif.meta['nodata']) as destination:
        destination.write(Result)
        
    SeedTif.close()
    
    return


#------------------------------------------------------------------------------
# Importing the input as a binary matrix starting from a .TIF
#------------------------------------------------------------------------------

def TakeImage(sizeR,sizeC):
    
    from PIL import Image
    im_Seed = Image.open('seed_binary.tif')
    imarray_Seed = np.array(im_Seed)
    
    im_Grow = Image.open('grow_binary.tif')
    imarray_Grow = np.array(im_Grow)
    
    im_Result = Image.open('result_binary.tif')
    imarray_Result = np.array(im_Result)
    
    Seed=imarray_Seed[0:sizeR,0:sizeC]
    Grow=imarray_Grow[0:sizeR,0:sizeC]
    Result=imarray_Result[0:sizeR,0:sizeC]
    
    return Seed, Grow, Result
    

#------------------------------------------------------------------------------
# Plot a color grid reading the value in the matrix: 
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
    # ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    # ax.set_xticks(np.arange(0.5, size, 1));
    # ax.set_yticks(np.arange(0.5, size, 1));

    plt.show()
  
    
#------------------------------------------------------------------------------
# Look for the 8 neighbors of a pixel, in our case the pixel in question
# is a seed and we go to select its neighbors
#------------------------------------------------------------------------------

#copy() necessario altrimenti python crea non una copia ma un collegamento
#e se modifivco uno allora modifico pure l'altro se si tratta di array

def CercaVicini(Raster,sizeR,sizeC):
    
    MatriceVicini=Raster[:,:].copy()
   
    #set the seed's neighbours to 1 
    #row
    for j in range(sizeR): 
        #column
        for k in range(sizeC):
            
            #element inside the matrix
            if Raster[j,k]==1 and j>0 and j<sizeR-1 and k>0 and k<sizeC-1:
                
                MatriceVicini[j-1:j+2,k-1:k+2]=1               
            
            #first row without corners
            if Raster[j,k]==1 and j==0 and k>0 and k<sizeC-1:
                
                MatriceVicini[j:j+2,k-1:k+2]=1
                
            #last row without corners
            if Raster[j,k]==1 and j==sizeR-1 and k>0 and k<sizeC-1:
                
                MatriceVicini[j-1:j+1,k-1:k+2]=1
       
            #first column without corners
            if Raster[j,k]==1 and j>0 and j<sizeR-1 and k==0:           
          
                MatriceVicini[j-1:j+2,k:k+2]=1
           
            #last column without corners
            if Raster[j,k]==1 and j>0 and j<sizeR-1 and k==sizeC-1:
          
                MatriceVicini[j-1:j+2,k-1:k+1]=1
              
            #upper-left corner
            if Raster[j,k]==1 and j==0 and k==0:            
               
                MatriceVicini[j:j+2,k:k+2]=1
            
            #upper-right corner
            if Raster[j,k]==1 and j==0 and k==sizeC-1:      
                         
                MatriceVicini[j:j+2,k-1:k+1]=1               
            
            #lower-left corner
            if Raster[j,k]==1 and j==sizeR-1 and k==0:               

                MatriceVicini[j-1:j+1,k:k+2]=1
            
            #lower-right corner
            if Raster[j,k]==1 and j==sizeR-1 and k==sizeC-1:
    
                MatriceVicini[j-1:j+1,k-1:k+2]=1
          
    return MatriceVicini
          
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



