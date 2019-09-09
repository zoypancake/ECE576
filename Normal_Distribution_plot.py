#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def show_hist_line (loc,scale):
    sample = np.random.normal(loc = loc, scale=scale, size=1000000)
    xindex = np.arange(loc-5*scale,loc+5*scale,0.01)
    yindex = scipy.stats.norm.pdf(xindex,loc=loc,scale=scale)
    plt.hist(sample,bins=100,density=True)
    plt.plot(xindex,yindex)
    plt.show()


if __name__ == "__main__":
    loc = float(input("Enter the mean of normal distribution: "))
    scale = float(input("Enter the standard deviation of normal distribution: "))
    show_hist_line(loc,scale)
