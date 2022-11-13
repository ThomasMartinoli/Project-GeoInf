# -*- coding: utf-8 -*-
"""
@author: thmar
"""

#STATISTICS


import numpy as np
from Function import *
from RegionGrowing_LayerSum import *
from RegionGrowing_pixelBypixel import *
import time
import matplotlib.pyplot as plt
import os
import rasterio

dimension=np.array([200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400])
#dimension=np.array([0,400])

#-----------------------------------------------------------------------------
# Open TIF file
#-----------------------------------------------------------------------------

path = os.getcwd()
Seed_file = "\\seed_binary.tif"
Grow_file = "\\grow_binary.tif"

SeedTif=rasterio.open(path+Seed_file)
GrowTif=rasterio.open(path+Grow_file)

# Read the file .tif 

Seed_array = SeedTif.read()
Grow_array = GrowTif.read()

#-----------------------------------------------------------------------------
#RegionGrowing_LayerSum
#-----------------------------------------------------------------------------

print('Region Growing Layer Sum \n')


mean_LS=np.array([])
var_LS=np.var([])

for size in dimension:
    
    sizeR=size
    sizeC=size
        
    T=np.ones((sizeR,sizeC))*-1
    Raster=np.array([Seed_array[:,0:sizeR,0:sizeC],Grow_array[:,0:sizeR,0:sizeC],T])
    tempi_LS=np.array([])
    
    for i in range(1):
        start_LS=time.process_time()
        print('Output:',size , "pixel",'\n')
        Burned_LS, seed_array_LS, iterazioni_LS=RG_LS(Raster,sizeR,sizeC)
        
        print('-----------------------')
        end_LS=time.process_time()
        delta_LS=(end_LS-start_LS)
        print('delta:',delta_LS)
        tempi_LS=np.append(tempi_LS,delta_LS)
        
    mean=np.mean(tempi_LS)
    mean_LS=np.append(mean_LS,mean)
        
    var=np.var(tempi_LS)
    var_LS=np.append(var_LS,var)

print('-----------------------')

#-----------------------------------------------------------------------------
#RegionGrowing_PixelbyPixel
#-----------------------------------------------------------------------------

print('Region Growing Pixel by Pixel\n')


mean_PP=np.array([])
var_PP=np.var([])

for size in dimension:
    
    sizeR=size
    sizeC=size
    
    
    T=np.ones((sizeR,sizeC))*-1
    Raster=np.array([Seed_array[:,0:sizeR,0:sizeC],Grow_array[:,0:sizeR,0:sizeC],T])
    tempi_PP=np.array([])
    
    for i in range(1):
        start_PP=time.process_time()
        print('Output:',size ,"pixel",'\n')
        Burned_PP, seed_array_PP, iterazioni_PP=RG_PP(Raster,sizeR,sizeC)
        print('-----------------------')
        end_PP=time.process_time()
        delta_PP=(end_PP-start_PP)
        print('delta:',delta_PP)
        tempi_PP=np.append(tempi_PP,delta_PP)
        
    mean=np.mean(tempi_PP)
    mean_PP=np.append(mean_PP,mean)
        
    var=np.var(tempi_PP)
    var_PP=np.append(var_PP,var)
    
#-----------------------------------------------------------------------------
#Calcolo delle statistiche
#-----------------------------------------------------------------------------
    


fig, ax=plt.subplots()
ax.plot(dimension, mean_LS, marker = "o", color = 'red', label='LayerSum')
ax.plot(dimension, mean_PP, marker = "x", color = 'blue',label='PixelByPixel')
plt.title("Process Time")
plt.xlabel("Image Size") 
plt.ylabel("time [s]")
legend=ax.legend()
plt.show()


# fig2, ax=plt.subplots()
# ax.plot(iterazioni_LS, seed_array_LS, marker = "o", color = 'red', label='seed_LayerSum')
# ax.plot(iterazioni_PP, seed_array_PP, marker = "x", color = 'blue',label='seed_PixelByPixel')



# if iterazioni_PP[-1]>=iterazioni_LS[-1]:
#     plt.hlines(y=seed_array_PP[-1],xmin=iterazioni_PP[0],xmax=iterazioni_PP[-1],color='green',label='output')
# else:
#     plt.hlines(y=seed_array_LS[-1],xmin=iterazioni_LS[0],xmax=iterazioni_LS[-1],color='green',label='output')
# plt.title("Convergenza")
# plt.xlabel("step") 
# plt.ylabel("# seed")
# legend=ax.legend()
# plt.show()



#-----------------------------------------------------------------------------
# Close TIF file
#-----------------------------------------------------------------------------

SeedTif.close()
GrowTif.close()
