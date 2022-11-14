# -*- coding: utf-8 -*-
"""
@author: thmar
"""


import numpy as np
from Function import *
from RegionGrowing_LayerSum import *
from RegionGrowing_pixelBypixel import *
import time


#------------------------------------------------------------------------------
#Import Images from .TIF file
#------------------------------------------------------------------------------

sizeR=500
sizeC=500

OWAseed,OWAgrow,Result=TakeImage(sizeR,sizeC)

#------------------------------------------------------------------------------
#Inizialization to time at -1
#------------------------------------------------------------------------------

T=np.ones((sizeR,sizeC))*-1

Raster=np.array([OWAseed,OWAgrow,T])

#------------------------------------------------------------------------------
#RegionGrowing_LayerSum
#------------------------------------------------------------------------------

print('REGION GROWING LAYER SUM','\n')
print('seed_new|','seed_old|','iter','\n')

start = time.process_time()
Burned_LS, seed_array_LS, iterazioni_LS = RG_LS(Raster,sizeR,sizeC)

#tre output

ColorGrid(OWAseed,sizeR,sizeC)
ColorGrid(OWAgrow,sizeR,sizeC)
ColorGrid(Burned_LS,sizeR,sizeC)

end = time.process_time()

print('\n')
print('TEMPO SOMMA LAYER: ',(end - start)/60)
print('--------------------------------------------','\n')


#------------------------------------------------------------------------------
#RegionGrowing pixel_by_pixel
#------------------------------------------------------------------------------
start1 = time.process_time()

print('REGION GROWING PIXEL BY PIXEL','\n')
print('seed_new|','seed_old|','iter','\n')


Burned_PP, seed_array_PP, iterazioni_PP=RG_PP(Raster,sizeR,sizeC)
# ColorGrid(Raster[0],size)
# ColorGrid(Raster[1],size)
# ColorGrid(Burned_PP[0],size)

end1 = time.process_time()
print('\n')
print('TEMPO PIXEL BY PIXEL: ',(end1 - start1)/60)
print('--------------------------------------------')


#-----------------------------------------------------------------------------
#ERRORI rispetto alla soluzione proposta
#-----------------------------------------------------------------------------
    
Test=Burned_PP[0]-Result

A=np.count_nonzero(Test==0)
B=np.count_nonzero(Test==1)
C=np.count_nonzero(Test==-1)

print('-----------------------')
print('Errori')
commission_error=B/np.count_nonzero(Burned_PP[0])*100
print('Errore di commissione:',round(commission_error,2),'%')
omission_error=C/np.count_nonzero(Result)*100
print('Errore di omissione:',round(omission_error,2),'%')

#-----------------------------------------------------------------------------
#Statistic Computation
#-----------------------------------------------------------------------------

fig, ax=plt.subplots()
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
#Export the result as a .TIF file
#-----------------------------------------------------------------------------

ExportResult(Burned_PP[0],sizeR,sizeC)
