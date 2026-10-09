"""Regenerates docs/figures/period_radius.png from data/cumulative_cleaned.csv. Run from the repository root: python docs/make_period_radius_figure.py"""
import matplotlib as mpl
S=['#2a78d6','#eb6834','#1baf7a','#eda100']
INK='#0b0b0b'; INK2='#52514e'; GRID='#e4e3df'; SURF='#ffffff'
mpl.rcParams.update({'figure.facecolor':SURF,'axes.facecolor':SURF,'savefig.facecolor':SURF,
 'font.family':'DejaVu Sans','font.size':11,'axes.edgecolor':GRID,'axes.labelcolor':INK2,
 'xtick.color':INK2,'ytick.color':INK2,'axes.titlecolor':INK,'axes.titlesize':13,'axes.titleweight':'bold',
 'axes.titlelocation':'left','axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.color':GRID,
 'grid.linewidth':0.8,'axes.axisbelow':True,'legend.frameon':False,'legend.labelcolor':INK2})

import pandas as pd, numpy as np, matplotlib.pyplot as plt
d=pd.read_csv('data/cumulative_cleaned.csv')
d=d[(d.koi_period>0)&(d.koi_prad>0)]
cls=[('CONFIRMED','Confirmed',S[0]),('CANDIDATE','Candidate',S[2]),('FALSE POSITIVE','False positive',S[1])]
fig,axes=plt.subplots(1,3,figsize=(13,4.6),sharex=True,sharey=True)
for ax,(k,name,c) in zip(axes,cls):
    ax.scatter(d.koi_period,d.koi_prad,s=3,color='#d6d5d0',lw=0,rasterized=True)
    g=d[d.koi_disposition==k]
    ax.scatter(g.koi_period,g.koi_prad,s=4,color=c,alpha=0.6,lw=0,rasterized=True)
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_title(f'{name}  (n = {len(g):,})'.replace(',', ' ') if False else f'{name}  (n = {len(g):,})',fontsize=12)
    for y,lab in [(1.25,'Earth'),(2,'Super-Earth'),(6,'Neptune'),(15,'Jupiter')]:
        ax.axhline(y,color=INK2,lw=0.7,ls=(0,(3,3)),zorder=1)
    ax.set_xlabel('Orbital period (days)')
    ax.grid(False)
from matplotlib.ticker import FuncFormatter
fmt=FuncFormatter(lambda v,_: f'{v:g}')
for ax in axes: ax.xaxis.set_major_formatter(fmt); ax.yaxis.set_major_formatter(fmt)
axes[0].set_ylabel('Planet radius (Earth radii)')
fig.suptitle('Kepler objects in the period-radius plane',x=0.01,ha='left',fontsize=14,fontweight='bold',color=INK)
fig.text(0.01,0.865,'Dashed lines: size-class boundaries at 1.25, 2, 6 and 15 Earth radii. Above 15, objects are almost all false positives.',color=INK2,fontsize=10)
fig.tight_layout(rect=(0,0,1,0.87)); fig.savefig('docs/figures/period_radius.png',dpi=150)
