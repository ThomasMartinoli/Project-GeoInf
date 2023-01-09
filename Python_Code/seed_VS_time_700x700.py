# -*- coding: utf-8 -*-
"""
in questo file vengono applicati gli algoritmi implementati a 5 clip random per verificare un 
evntuale relazione tra: numero di semi iniziale e tempo di processo

le immagini hanno dimensione 700*700 pixel
"""

import numpy as np
from Function import *
from RegionGrowing_LayerSum import *
from RegionGrowing_pixelBypixel import *
import time
import matplotlib.pyplot as plt
from PIL import Image

size=700
sizeR=size
sizeC=size
indice_LS=np.array([1,2,3,4,5])
indice_PP=np.array([1,2,3,4,5])

#-----------------------------------------------------------------------------
# Read the input images
#-----------------------------------------------------------------------------
im_Seed_1 = Image.open('images\clip\clip_seed_1.tif')
imarray_Seed_1 = np.array(im_Seed_1)

im_Seed_2 = Image.open('images\clip\clip_seed_2.tif')
imarray_Seed_2 = np.array(im_Seed_2)

im_Seed_3 = Image.open('images\clip\clip_seed_3.tif')
imarray_Seed_3 = np.array(im_Seed_3)

im_Seed_4 = Image.open('images\clip\clip_seed_4.tif')
imarray_Seed_4 = np.array(im_Seed_4)

im_Seed_5 = Image.open('images\clip\clip_seed_5.tif')
imarray_Seed_5 = np.array(im_Seed_5)


   
im_Grow_1 = Image.open('images\clip\clip_grow_1.tif')
imarray_Grow_1 = np.array(im_Grow_1)

im_Grow_2 = Image.open('images\clip\clip_grow_2.tif')
imarray_Grow_2 = np.array(im_Grow_2)

im_Grow_3 = Image.open('images\clip\clip_grow_3.tif')
imarray_Grow_3 = np.array(im_Grow_3)

im_Grow_4 = Image.open('images\clip\clip_grow_4.tif')
imarray_Grow_4 = np.array(im_Grow_4)

im_Grow_5 = Image.open('images\clip\clip_grow_5.tif')
imarray_Grow_5 = np.array(im_Grow_5)

#-----------------------------------------------------------------------------
# Input images become binary matrix
#-----------------------------------------------------------------------------

Seed_1=imarray_Seed_1[0:size,0:size]
Seed_2=imarray_Seed_2[0:size,0:size]
Seed_3=imarray_Seed_3[0:size,0:size]
Seed_4=imarray_Seed_4[0:size,0:size]
Seed_5=imarray_Seed_5[0:size,0:size]


Grow_1=imarray_Grow_1[0:size,0:size]
Grow_2=imarray_Grow_2[0:size,0:size]
Grow_3=imarray_Grow_3[0:size,0:size]
Grow_4=imarray_Grow_4[0:size,0:size]
Grow_5=imarray_Grow_5[0:size,0:size]

#-----------------------------------------------------------------------------
# Data are reordering and collecting in an array
#-----------------------------------------------------------------------------

T=np.ones((size,size))*-1

Raster_1=np.array([Seed_1,Grow_1,T])
Raster_2=np.array([Seed_2,Grow_2,T])
Raster_3=np.array([Seed_3,Grow_3,T])
Raster_4=np.array([Seed_4,Grow_4,T])
Raster_5=np.array([Seed_5,Grow_5,T])


#------------------------------------------------------------------------------
# Using RegionGrowing_LayerSum
#------------------------------------------------------------------------------

print('REGION GROWING LAYER SUM','\n')
print('seed_new|','seed_old|','iter','\n')

time_LS=np.array([])
seed_iniziali_LS=np.array([])

# 1 clip
start = time.process_time()
seed=np.count_nonzero(Raster_1[0])
seed_iniziali_LS=np.append(seed_iniziali_LS, seed)
RG_LS(Raster_1,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_LS=np.append(time_LS, delta)

# 2 clip
start = time.process_time()
seed=np.count_nonzero(Raster_2[0])
seed_iniziali_LS=np.append(seed_iniziali_LS, seed)
RG_LS(Raster_2,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_LS=np.append(time_LS, delta)

# 3 clip
start = time.process_time()
seed=np.count_nonzero(Raster_3[0])
seed_iniziali_LS=np.append(seed_iniziali_LS, seed)
RG_LS(Raster_3,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_LS=np.append(time_LS, delta)

# 4 clip
start = time.process_time()
seed=np.count_nonzero(Raster_4[0])
seed_iniziali_LS=np.append(seed_iniziali_LS, seed)
RG_LS(Raster_4,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_LS=np.append(time_LS, delta)

#♦ 5 clip
start = time.process_time()
seed=np.count_nonzero(Raster_5[0])
seed_iniziali_LS=np.append(seed_iniziali_LS, seed)
RG_LS(Raster_5,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_LS=np.append(time_LS, delta)



#-----------------------------------------------------------------------------
# Using RegionGrowing pixel_by_pixel
#-----------------------------------------------------------------------------

print('REGION GROWING PIXEL BY PIXEL','\n')
print('seed_new|','seed_old|','iter','\n')


time_PP=np.array([])
seed_iniziali_PP=np.array([])

# 1 clip
start = time.process_time()
seed=np.count_nonzero(Raster_1[0])
seed_iniziali_PP=np.append(seed_iniziali_PP, seed)
RG_PP(Raster_1,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_PP=np.append(time_PP, delta)

# 2 clip
start = time.process_time()
seed=np.count_nonzero(Raster_2[0])
seed_iniziali_PP=np.append(seed_iniziali_PP, seed)
RG_PP(Raster_2,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_PP=np.append(time_PP, delta)

# 3 clip
start = time.process_time()
seed=np.count_nonzero(Raster_3[0])
seed_iniziali_PP=np.append(seed_iniziali_PP, seed)
RG_PP(Raster_3,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_PP=np.append(time_PP, delta)

# 4 clip
start = time.process_time()
seed=np.count_nonzero(Raster_4[0])
seed_iniziali_PP=np.append(seed_iniziali_PP, seed)
RG_PP(Raster_4,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_PP=np.append(time_PP, delta)

# 5 clip
start = time.process_time()
seed=np.count_nonzero(Raster_5[0])
seed_iniziali_PP=np.append(seed_iniziali_PP, seed)
RG_PP(Raster_5,sizeR,sizeC)
end = time.process_time()
delta=end-start
time_PP=np.append(time_PP, delta)


#-----------------------------------------------------------------------------
# Output
#-----------------------------------------------------------------------------
# I rearrange the two vectors in ascending order with respect to the number 
# of seeds and consequently the relative times

# riordino i due vettori in ordine crescente rispetto al numero di semi e 
# di conseguenza i relativi tempi

x_LS, y_LS, index_LS = (list(t) for t in zip(*sorted(zip(seed_iniziali_LS,time_LS,indice_LS))))
x_PP, y_PP, index_PP = (list(t) for t in zip(*sorted(zip(seed_iniziali_PP,time_PP,indice_PP))))


fig, ax=plt.subplots()
ax.plot(x_LS, y_LS, marker = "o", color = 'red', label='LayerSum')
ax.plot(x_PP, y_PP, marker = "x", color = 'blue',label='PixelByPixel')
plt.title("#seed VS time")
plt.xlabel("# seed") 
plt.ylabel("time [s]")
legend=ax.legend()
plt.show()

