# -*- coding: utf-8 -*-
"""
This file is used in order to compute some comparison between the two methods

"""

#STATISTICHE

#------------------------------------------------------------------------------
# Importing the libraries
#------------------------------------------------------------------------------

import numpy as np
from Function import *
from RegionGrowing_LayerSum import *
#from RegionGrowing_pixelBypixel import *
from RegionGrowing_pixelBypixel_condition import *
import time
import matplotlib.pyplot as plt

dimension=np.array([200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400])
#dimension=np.array([0,700])

#-----------------------------------------------------------------------------
#RegionGrowing_LayerSum
#-----------------------------------------------------------------------------

# print('Region Growing Layer Sum \n')


# mean_LS=np.array([])
# var_LS=np.var([])

# for size in dimension:
    
#     sizeR=size
#     sizeC=size
#     print('LS', size)
    
    
#     OWAseed,OWAgrow,Result=TakeImage(sizeR,sizeC)
#     T=np.ones((sizeR,sizeC))*-1
#     Raster=np.array([OWAseed,OWAgrow,T])
#     tempi_LS=np.array([])
    
#     for i in range(1):
#         start_LS=time.process_time()
#         print('Output:',i+1,'\n')
#         Burned_LS, seed_array_LS, iterazioni_LS=RG_LS(Raster,sizeR,sizeC)
#         print(seed_array_LS)
#         print('-----------------------')
#         end_LS=time.process_time()
#         delta_LS=(end_LS-start_LS)
#         print('delta:',delta_LS)
#         tempi_LS=np.append(tempi_LS,delta_LS)
        
#     mean=np.mean(tempi_LS)
#     mean_LS=np.append(mean_LS,mean)
        
#     var=np.var(tempi_LS)
#     var_LS=np.append(var_LS,var)

# print('-----------------------')
#-----------------------------------------------------------------------------
#RegionGrowing_PixelbyPixel
#-----------------------------------------------------------------------------

print('Region Growing Pixel by Pixel\n')

mean_PP=np.array([])
var_PP=np.var([])

for size in dimension:
    
    print('PP', size)
    sizeR=size
    sizeC=size
    
    OWAseed,OWAgrow,Result=TakeImage(sizeR,sizeC)
    T=np.ones((sizeR,sizeC))*-1
    Raster=np.array([OWAseed,OWAgrow,T])
    tempi_PP=np.array([])
    
    for i in range(1):
        start_PP=time.process_time()
        print('Output:',i+1,'\n')
        Burned_PP, seed_array_PP, iterazioni_PP=RG_PP(Raster,sizeR,sizeC)
        print(seed_array_PP)
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
# Statistics computation 
#-----------------------------------------------------------------------------
  

fig, ax=plt.subplots()
ax.plot(dimension, mean_PP_1, marker = "o", color = 'red', label='PixelByPixel with T')
ax.plot(dimension, mean_PP, marker = "x", color = 'blue',label='PixelByPixel without T')
plt.title("Process Time")
plt.xlabel("Image Size") 
plt.ylabel("time [s]")
legend=ax.legend()
plt.show()


fig2, ax=plt.subplots()
ax.plot(iterazioni_LS, seed_array_LS, marker = "o", color = 'red', label='seed_LayerSum')
ax.plot(iterazioni_PP, seed_array_PP, marker = "x", color = 'blue',label='seed_PixelByPixel')



if iterazioni_PP[-1]>=iterazioni_LS[-1]:
    plt.hlines(y=seed_array_PP[-1],xmin=iterazioni_PP[0],xmax=iterazioni_PP[-1],color='green',label='output')
else:
    plt.hlines(y=seed_array_LS[-1],xmin=iterazioni_LS[0],xmax=iterazioni_LS[-1],color='green',label='output')
plt.title("Convergenza")
plt.xlabel("step") 
plt.ylabel("# seed")
legend=ax.legend()
plt.show()


#-----------------------------------------------------------------------------
# Errors with respect to the proposed solution
#-----------------------------------------------------------------------------
    
Test=Burned_PP[0]-Result

A=np.count_nonzero(Test==0)
B=np.count_nonzero(Test==1)
C=np.count_nonzero(Test==-1)

print('-----------------------')
print('Errori')
commission_error=B/np.count_nonzero(Burned_PP)*100
print('Errore di commissione:',round(commission_error,2),'%')
omission_error=C/np.count_nonzero(Result)*100
print('Errore di omissione:',round(omission_error,2),'%')
