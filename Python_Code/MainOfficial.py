# -*- coding: utf-8 -*-
"""
@author: thmar
"""

import numpy as np
import array
from Function_Update_12_11_22 import *
from RegionGrowing_LayerSum_Update_12_11_22 import *
from RegionGrowing_pixelBypixel_Update_12_11_22 import *
import pylab as pl
import time
import rasterio
from matplotlib import pyplot
import os

#------------------------------------------------------------------------------
#Importare dati da Qgis
#------------------------------------------------------------------------------

# Open the file .tif

path = os.getcwd()
Seed_file = "\\seed_binary.tif"
Grow_file = "\\grow_binary.tif"
Result_file = "\\result_binary.tif"


SeedTif=rasterio.open(path+Seed_file)
GrowTif=rasterio.open(path+Grow_file)
ResultTif=rasterio.open(path+Result_file)


sizeR=500
sizeC=500

# Read the file .tif 

Seed_array = SeedTif.read()
Grow_array = GrowTif.read()
Result_array = ResultTif.read()

#inizializzo time a -1

T=np.ones((sizeR,sizeC))*-1

#inizialmente considero solo i semi come pixel bruciati 
#quindi inizializzo k con gli stessi valori del layer seed

Raster=np.array([Seed_array[:,0:sizeR,0:sizeC],Grow_array[:,0:sizeR,0:sizeC],T])

#------------------------------------------------------------------------------
#RegionGrowing_LayerSum
#------------------------------------------------------------------------------

print('REGION GROWING LAYER SUM','\n')
print('seed_new|','seed_old|','iter','\n')

start = time.process_time()
Burned_LS, seed_array_LS, iterazioni_LS = RG_LS(Raster,sizeR,sizeC)


pyplot.imshow(Seed_array[0][0:sizeR,0:sizeC], cmap='hot_r')
pyplot.show() 
pyplot.imshow(Grow_array[0][0:sizeR,0:sizeC], cmap='hot_r')
pyplot.show() 
pyplot.imshow(Burned_LS[0], cmap='hot_r')
pyplot.show() 


LS_File="\\LS_Result.tif"
LS_File_Out=path+LS_File
with rasterio.open(LS_File_Out,
                   'w',                    
                   driver = SeedTif.meta['driver'],
                   height = SeedTif.meta['height'],
                   width=SeedTif.meta['width'],
                   count=SeedTif.meta['count'],
                   crs=SeedTif.meta['crs'],
                   transform=SeedTif.meta['transform'],
                   dtype= SeedTif.meta['dtype'],
                   nodata= SeedTif.meta['nodata']) as destination:
    destination.write(Burned_LS)


end = time.process_time()


print('\n')
print('COMPUTATIONAL TIME LAYER SUM: ',(end - start)/60)
print('--------------------------------------------','\n')

#------------------------------------------------------------------------------
#RegionGrowing pixel_by_pixel
#------------------------------------------------------------------------------
start1 = time.process_time()

print('REGION GROWING PIXEL BY PIXEL','\n')
print('seed_new|','seed_old|','iter','\n')

Burned_PP, seed_array_PP, iterazioni_PP=RG_PP(Raster,sizeR,sizeC)

PP_File="\\PP_Result.tif"
PP_File_Out=path+PP_File
with rasterio.open(PP_File_Out,
                   'w',                    
                   driver = SeedTif.meta['driver'],
                   height = SeedTif.meta['height'],
                   width=SeedTif.meta['width'],
                   count=SeedTif.meta['count'],
                   crs=SeedTif.meta['crs'],
                   transform=SeedTif.meta['transform'],
                   dtype= SeedTif.meta['dtype'],
                   nodata= SeedTif.meta['nodata']) as destination:
    destination.write(Burned_PP[0])

end1 = time.process_time()

print('\n')
print('COMPUTATIONAL TIME PIXEL BY PIXEL: ',(end1 - start1)/60)
print('--------------------------------------------')

#-----------------------------------------------------------------------------
#ERRORI rispetto alla soluzione proposta
#-----------------------------------------------------------------------------
    
Test=Burned_PP[0]-Result_array[0][0:sizeR,0:sizeC]

A=np.count_nonzero(Test==0)
B=np.count_nonzero(Test==1)
C=np.count_nonzero(Test==-1)

print('-----------------------')
print('Errors')
commission_error=B/np.count_nonzero(Burned_PP[0])*100
print('Commission Error:',round(commission_error,2),'%')
omission_error=C/np.count_nonzero(Result_array[0])*100
print('Omission Error:',round(omission_error,2),'%')

#-----------------------------------------------------------------------------
#Convergence computation
#-----------------------------------------------------------------------------

fig, ax=plt.subplots()
ax.plot(iterazioni_LS, seed_array_LS, marker = "o", color = 'red', label='seed_LayerSum')
ax.plot(iterazioni_PP, seed_array_PP, marker = "x", color = 'blue',label='seed_PixelByPixel')


if iterazioni_PP[-1]>=iterazioni_LS[-1]:
    plt.hlines(y=seed_array_PP[-1],xmin=iterazioni_PP[0],xmax=iterazioni_PP[-1],color='green',label='output')
else:
    plt.hlines(y=seed_array_LS[-1],xmin=iterazioni_LS[0],xmax=iterazioni_LS[-1],color='green',label='output')
plt.title("Convergences")
plt.xlabel("step") 
plt.ylabel("# seed")
legend=ax.legend()
plt.show()

