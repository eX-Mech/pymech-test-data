#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: manu
date: 26-04-2021
"""
#from pymech.neksuite import readnek
from pymech.dataset import open_dataset
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
plt.rcParams['svg.fonttype'] = 'none'  # outputs text as text in svg file
plt.rcParams["figure.figsize"] = (5.75, 4.25)
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['legend.frameon'] = 1
plt.rcParams['legend.facecolor'] = 'white'
plt.rcParams['grid.alpha'] = 0.2
plt.rcParams['figure.frameon'] = False
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["axes.formatter.min_exponent"] = True

#plt.rcParams["figure.autolayout"] = True


#field = readnek('meaABL0.f00001')
#[attr for attr in dir(field) if not attr.startswith('__')]
#
##print(field.endian, field.istep, field.lr1, field.nbc, field.ncurv, field.ndim, field.nel, field.time, field.var, field.wdsz)
#
#print("There are", field.nel, "elements in this file")


#ds = open_dataset('./ABL_new0.f00001')
#ds = open_dataset('./avgABL0.f00001')
ds = open_dataset('./turbChannel0.f00001')
# %%

w, h = plt.figaspect(0.17)
plt.figure(figsize=(w, h), frameon=False)
#ds.uz.mean("z").plot(levels=np.linspace(0, 15, 1000), cmap='rainbow')
ds.uz.mean("x").plot(x="z", levels=np.linspace(4, 15, 1100), cmap="plasma",
                     cbar_kwargs={"aspect": 8, "ticks": [5, 7, 9, 11, 13, 15], "label": "Streamwise velocity (m/s)"})
#ds.uz.isel(x=0).plot(x="z", levels=np.linspace(0, 15, 1000), cmap='rainbow')
plt.title(None)
plt.tight_layout()
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("Streamwise distance (m)")
plt.ylabel("y (m)")
plt.savefig("uz_contour.png")
plt.show()

# %%

# data from gregoire :
y = np.array([0.5195320180813313, 0.567716130643088, 0.6203695712190365, 0.6779066747653637, 0.7407798553730089, 0.8094844336162585, 0.8845609343918978, 0.9666010486371028, 1.0562492930783787, 1.1542122650367246, 1.2612609177503606, 1.3782384475813918, 1.5060631865229477, 1.6457347246688576, 1.7983582831628306, 1.9651359761343685, 2.1473800249335677, 2.3465255955601956, 2.5641471663494393, 2.8019677255750657, 3.061846356742775, 3.34582837151521, 3.656142226983371, 3.9952257455728875, 4.3657604554429685, 4.770662953612035, 5.213120162374675, 5.696609939248663, 6.224927583587238, 6.802249311508431, 7.433111005349033, 8.122476037944372, 8.875776205745655, 9.698935681244198, 10.598434762749982, 11.581355224108245,
              12.655436191321904, 13.829132531422411, 15.11168623039136, 16.513194076362737, 18.04467539641722, 19.718198374628944, 21.546929418215942, 23.545276751295972, 25.72893872736288, 28.115136661921092, 30.722615651715362, 33.571945847149465, 36.685505083783525, 40.08785593030522, 43.80570248071803, 47.8683698696464, 52.30779030133338, 57.15894367979372, 62.45992009148288, 65.55529665310557, 86.92949626213681, 94.99134910388193, 103.80089953739737, 113.42749661103043, 123.94682559592067, 135.44172298881185, 148.00254860654732, 161.728324302649, 176.72706454177435, 193.11720552248414, 211.0278627272319, 230.59937539279014, 251.98572974962983, 275.35486579149887, 300.890494172574, 328.79358586824407, 347.8814678825292])

u = np.array([4.056740325097536, 4.203204503952639, 4.353035675425097, 4.504550343206239, 4.6543815146787, 4.8050544343055, 4.95488560577796, 5.107242021713441, 5.256231445031563, 5.4060626165040215, 5.555893787976483, 5.707408455757625, 5.853030886458386, 5.976767865146318, 6.097979599371229, 6.219191333596145, 6.339561319666716, 6.460773053891629, 6.594611010431635, 6.753701411601833, 6.913633560926369, 7.073565710250907, 7.225080378032045, 7.364810571652431, 7.507907757890175, 7.653530188590937, 7.800836115600379, 7.945616798146801, 8.081138250995489, 8.220868444615872, 8.358915141927579, 8.494436594776264, 8.630799795779291, 8.765479500473637, 8.899317457013645, 9.033155413553652, 9.167835118247998,
              9.303356571096685, 9.44056152025405, 9.579449965720096, 9.716654914877463, 9.855543360343507, 9.994431805809551, 10.135845495738616, 10.273892193050322, 10.414464134825046, 10.551669083982413, 10.692241025757136, 10.829445974914503, 10.970017916689226, 11.105539369537912, 11.24274431869528, 11.377424023389626, 11.512945476238311, 11.64257469200662, 11.682978603414924, 12.140889599375704, 12.267151822526653, 12.395097541986283, 12.524726757754593, 12.652672477214221, 12.780618196673851, 12.905196923516122, 13.031459146667071, 13.158563117972362, 13.294926318975389, 13.44054874967615, 13.581120691450876, 13.716642144299561, 13.842062619296172, 13.956540368286367, 14.062600635733165, 14.115069604020338])

line = ds.uz.mean(['x', 'z'])
plt.figure(frameon=False)
line.plot.line("-")
plt.semilogx(y, u)
plt.xscale('log')
plt.ylim(2, 16)
plt.xlim(1e-1, 1e+3)
plt.grid(which="both")

y_mesh = np.array(ds.ymesh.isel(x=0, z=0))
uniques, counts = np.unique(y_mesh, return_counts=True)
elm = uniques[np.where(counts > 1)]
for i in range(len(elm)):
    index = (np.abs(y_mesh - elm[i])).argmin()
    local_vel = line.isel(y=index)
    plt.plot([elm[i], elm[i]], [local_vel-2, local_vel+2], "C7-", alpha=0.2)

plt.legend([r"$\langle \overline{u} \rangle$",
            "gregoire's simulation", "mesh element size"])
plt.title(None)
plt.ylabel("Streamwise velocity (m/s)")
plt.xlabel("y (m)")
plt.savefig("uz_line.svg")
plt.show()

# %%
# w, h = plt.figaspect(0.5)
# plt.figure(figsize=(w, h), frameon=False)
# #plt.figure(frameon=False)
# #line.plot.line("-")
# plt.plot(line, line.y, '-')
# plt.xlim(2, 15)
# plt.xlabel("Streamwise velocity (m/s)")
# plt.ylabel("y (m)")
# plt.grid(which="both")
# plt.savefig("uz_line2.png")
# plt.show()
#
