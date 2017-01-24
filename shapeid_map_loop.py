# -*- coding: utf-8 -*-
"""
@author: Connor
"""

import numpy as np
import pandas as pd
from matplotlib.mlab import griddata
#from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree as KDTree
import pdb

import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9

zones = pd.read_csv('congress_shapes_final.csv')
shapeids = list(set(zones['shapeid']))

"""
no, no,no I need to use a patches collection
remember to do this tomorrow, not gonna finish tonight
I need to sleep so that I can work and still do this after
this technically works, but I want to assign values to the patches and such,
should probably just use bokeh for this, generate an html file

"""

for sid in shapeids:
    sid_df = zones[zones['shapeid'] == sid]
    plt.plot(sid_df['x'], sid_df['y'], color = 'k', linewidth = 0.1)
#plt.show()
#print(t)
plt.savefig('congress_test.png', dpi=500)
