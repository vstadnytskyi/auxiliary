#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
plotting functions
author: Valentyn Stadnytskyi
data: 2017 - Nov 17 2018

"""
__vesrion__ = '1.0.0'
from time import  time, sleep
import sys
if sys.version_info[0] == 2:
    from time import clock as perf_counter
else:
    from time import perf_counter
import platform
from ubcs_auxiliary.save_load_object import save_to_file, load_from_file

#def generate_plot(x,y):#
    #from matplotlib.figure import Figure
    #from matplotlib import pyplot
    #from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
    #figure = Figure(figsize=(8,3),dpi=80)
    #axis = figure.add_subplot(1,1,1)
    #axis.plot(x,y)
    #return axis

def generate_plot(x,y):
    from matplotlib.figure import Figure
    from matplotlib import pyplot as plt
    #from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
    figure = plt.figure()
    axis = figure.add_subplot(1,1,1)
    axis.plot(x,y)
    return figure

def plot_frames_as_RGB(frames = (None,None,None)):
    """
    takes a tuple of 3 mono-color frames and plots them as RGB. where RGB encoded the order of the supplied frames.

    All frames have to be the same size. Currently works for 3000x4096 size only.


    """
    from matplotlib import pyplot as plt
    from numpy import zeros, ones
    img = ones(frames[0].shape+(3,))
    for i in range(3):
        img[:,:,i] = frames[i]
    fig = plt.figure(figsize=(4, 4))
    grid = plt.GridSpec(1, 1, hspace=0.025, wspace=0.025)
    ax1 = fig.add_subplot(grid[0,0])
    ax1.imshow(img)

def plot_image_with_mask(image,mask):
    """
    plot an image and overlay a mask over it. The mask shows
    """
    from matplotlib import pyplot as plt
    from numpy import where
    fig = plt.figure(figsize=(4, 4))
    grid = plt.GridSpec(1, 1, hspace=0.025, wspace=0.025)
    ax1 = fig.add_subplot(grid[0,0])
    ax1.imshow(image)
    #fig.colorbar(cax = ax1,orientation='vertical', pad=0.0, shrink=0.855)
    xy_coordinates = where(mask)
    ax1.plot(xy_coordinates[1],xy_coordinates[0],'wo',markersize=3)

def plot_images(lst = [], vmax = None, vmin = None, titles = None):
    from matplotlib import pyplot as plt

    if vmax is None:
        vmax = []
        for item in lst:
            vmax.append(None)
    if vmin is None:
        vmin = []
        for item in lst:
            vmin.append(None)
    if titles is None:
        titles = []
        for item in lst:
            titles.append(None)

    fig = plt.figure(figsize=(7, 3))
    grid = plt.GridSpec(1, len(lst), hspace=0.025, wspace=0.025)
    ax = []
    ax.append(fig.add_subplot(grid[0,0]))
    ax[0].imshow(lst[0],vmax = vmax[0], vmin = vmin[0])
    ax[0].set_title(titles[0])
    ax[0].set_axis_off()
    for i in range(1,len(lst)):
        ax.append(fig.add_subplot(grid[0,i], sharex = ax[0], sharey = ax[0]))
        ax[i].imshow(lst[i],vmax = vmax[i], vmin = vmin[i])
        ax[i].set_title(titles[i])
        ax[i].set_axis_off()

def plot_images_grid(lst = [], vmax = None, vmin = None, titles = None):
    from matplotlib import pyplot as plt

    if vmax is None:
        vmax = []
        for item in lst:
            vmax.append(None)
    if vmin is None:
        vmin = []
        for item in lst:
            vmin.append(None)
    if titles is None:
        titles = []
        for item in lst:
            titles.append(None)

    fig = plt.figure(figsize=(7, 3))
    grid = plt.GridSpec(1, len(lst), hspace=0.025, wspace=0.025)
    ax = []
    ax.append(fig.add_subplot(grid[0,0]))
    ax[0].imshow(lst[0],vmax = vmax[0], vmin = vmin[0])
    ax[0].set_title(titles[0])
    ax[0].set_axis_off()
    for i in range(1,len(lst)):
        ax.append(fig.add_subplot(grid[0,i], sharex = ax[0], sharey = ax[0]))
        ax[i].imshow(lst[i],vmax = vmax[i], vmin = vmin[i])
        ax[i].set_title(titles[i])
        ax[i].set_axis_off()

if __name__ == '__main__':
    from numpy import arange, random
    #x = arange(0,100,1)
    #y = random.random((100,))
    #save_object('plot.pltpkl',generate_plot(x,y))
    #figure_loaded = load_object('plot.pltpkl')

    #figure_loaded.show()
