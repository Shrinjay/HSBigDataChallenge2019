# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import datetime 
from sklearn.linear_model import Ridge
flood = pd.read_csv("CDD.csv", index_col=False)


flood60 = (flood[(flood.Year<1970)&(flood.Year>1959)])
flood70 = (flood[(flood.Year<1980)&(flood.Year>1969)])
flood80 = (flood[(flood.Year<1990)&(flood.Year>1979)])
flood90 = (flood[(flood.Year<2000)&(flood.Year>1989)])
flood2000 = (flood[(flood.Year<2010)&(flood.Year>1999)])
flood2010 = (flood[(flood.Year<2020)&(flood.Year>2009)])




floodfreq1 = {'Decade':[1960, 1970, 1980, 1990, 2000, 2010], '# of Recorded Floods':[flood60['Year'].count(), flood70['Year'].count(), flood80['Year'].count(), flood90['Year'].count(), flood2000['Year'].count(), flood2010['Year'].count() ]}
floodfreq = pd.DataFrame(floodfreq1)

floodcost1 = {'Decade':[1960, 1970, 1980, 1990, 2000, 2010], 'Average ETC of Floods (CAD)':[flood60['ESTIMATEDTOTALCOST'].mean(),flood70['ESTIMATEDTOTALCOST'].mean(),flood80['ESTIMATEDTOTALCOST'].mean(), flood90['ESTIMATEDTOTALCOST'].mean(), flood2000['ESTIMATEDTOTALCOST'].mean(), flood2010['ESTIMATEDTOTALCOST'].mean() ]}
floodcost = pd.DataFrame(floodcost1)

floodfat1 = {'Decade':[1960, 1970, 1980, 1990, 2000, 2010], 'Total Fatalities due to Flooding':[flood60['FATALITIES'].sum(),flood70['FATALITIES'].sum(),flood80['FATALITIES'].mean(), flood90['FATALITIES'].sum(), flood2000['FATALITIES'].sum(), flood2010['FATALITIES'].sum() ]}
floodfat = pd.DataFrame(floodfat1)

floodfat1 = {'Decade':[1960, 1970, 1980, 1990, 2000, 2010], 'Total Fatalities due to Flooding':[flood60['FATALITIES'].sum(),flood70['FATALITIES'].sum(),flood80['FATALITIES'].mean(), flood90['FATALITIES'].sum(), flood2000['FATALITIES'].sum(), flood2010['FATALITIES'].sum() ]}
floodfat = pd.DataFrame(floodfat1)

floode1 = {'Decade':[1960, 1970, 1980, 1990, 2000, 2010], 'Total # of Persons Evacuated due to Flooding':[flood60['EVACUATED'].sum(),flood70['EVACUATED'].sum(),flood80['EVACUATED'].mean(), flood90['EVACUATED'].sum(), flood2000['EVACUATED'].sum(), flood2010['EVACUATED'].sum() ]}
floode = pd.DataFrame(floode1)
glacier = pd.read_csv("Glacier.csv", index_col=False)
PFlow = pd.read_csv("PFlow.csv", index_col=False)
precip = pd.read_csv("Precip.csv", index_col=False)

precip.dropna()
precip_clean = precip[['TotalPrecip']].copy()
PFPlot1 = PFlow.plot(x='Date', y='Mean Monthly Flow (m3/s)', kind='scatter')
PFPlot2 = PFlow.plot(x='Total Monthly Precipitation (mm)', y='Mean Monthly Flow (m3/s)', kind='scatter')
PFPlot3 = PFlow.plot(x='Date', y='Total Monthly Precipitation (mm)', kind='scatter')
PFPlot4 = PFlow.plot(x='Date', y='Mean Monthly Temperature (C)', kind='scatter')
PFPlot5 = PFlow.plot(x='Mean Monthly Temperature (C)', y='Total Monthly Precipitation (mm)', kind='scatter')
PFPlot6 = PFlow.plot(x='Mean Monthly Temperature (C)', y='Mean Monthly Flow (m3/s)', kind='scatter')
GPlot = glacier.plot(x='Mass Balance (m)', y='Mean Yearly Summer Flow (m3/s)', kind='scatter')
PFPlot7 = PFlow.plot(x=' Date', y='Mean Monthly Snowfall (mm)', kind='scatter')
GPlot2 = glacier.plot(x='Mean Yearly Snowfall (mm)', y='Mass Balance (m)', kind='scatter')
GPlot3 = glacier.plot(x='Mean Yearly Snowfall (mm)', y='Mean Yearly Summer Flow (m3/s)', kind='scatter')
GPlot4= glacier.plot(x='Year', y='Range (m3/s)', kind='scatter')
GPlot5 = glacier.plot(x='Year', y='Peak (m3/s)', kind='scatter')
GPlot6 = glacier.plot(x='Year', y='Min (m3/s)', kind='scatter')
GPlot7 = glacier.plot(x='Year', y='Mass Balance (m)', kind='scatter')
fig1= PFPlot1.get_figure()
fig1.savefig("Fig1.png")
fig2= PFPlot2.get_figure()
fig2.savefig("Fig2.png")
fig3= PFPlot3.get_figure()
fig3.savefig("Fig3.png")
fig4= GPlot.get_figure()
fig4.savefig("Fig4.png")
fig5= PFPlot4.get_figure()
fig5.savefig("Fig5.png")
fig6= PFPlot5.get_figure()
fig6.savefig("Fig6.png")
fig7= PFPlot6.get_figure()
fig7.savefig("Fig7.png")
fig8= PFPlot7.get_figure()
fig8.savefig("Fig8.png")
fig9= GPlot2.get_figure()
fig9.savefig("Fig9.png")
fig10= GPlot3.get_figure()
fig10.savefig("Fig10.png")
fig11= GPlot4.get_figure()
fig11.savefig("Fig11.png")
fig12= GPlot5.get_figure()
fig12.savefig("Fig12.png")
fig13= GPlot6.get_figure()
fig13.savefig("Fig13.png")
fig18= GPlot7.get_figure()
fig18.savefig("Fig18.png")
print(sp.stats.spearmanr(glacier['Mass Balance (m)'], glacier['Year']))
print(sp.stats.spearmanr(glacier['Mean Yearly Summer Flow (m3/s)'], glacier['Year']))
print(sp.stats.spearmanr(glacier['Mean Yearly Summer Flow (m3/s)'], glacier['Mass Balance (m)']))
print(sp.stats.spearmanr(glacier['Mean Yearly Snowfall (mm)'], glacier['Mass Balance (m)']))
print(sp.stats.spearmanr(glacier['Mean Yearly Snowfall (mm)'], glacier['Mean Yearly Summer Flow (m3/s)']))
print(sp.stats.spearmanr(glacier['Range (m3/s)'], glacier['Year']))
print(sp.stats.spearmanr(glacier['Peak (m3/s)'], glacier['Year']))
print(sp.stats.spearmanr(glacier['Min (m3/s)'], glacier['Year']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Snowfall (mm)'], PFlow[' Date']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Flow (m3/s)'], PFlow['Date']))
print(sp.stats.spearmanr(PFlow['Mean Flow Upstream of Edmonton (m3/s)'], PFlow['Date']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Flow (m3/s)'], PFlow['Total Monthly Precipitation (mm)']))
print(sp.stats.spearmanr(PFlow['Total Monthly Precipitation (mm)'], PFlow['Date']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Temperature (C)'], PFlow['Date']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Temperature (C)'], PFlow['Total Monthly Precipitation (mm)']))
print(sp.stats.spearmanr(PFlow['Mean Monthly Temperature (C)'], PFlow['Mean Monthly Flow (m3/s)']))
BFlow = pd.read_csv("BFlow.csv", index_col=False)
print(sp.stats.spearmanr(BFlow['MeanFlow'], BFlow['NumDate']))
print(sp.stats.spearmanr(BFlow['MeanFlow'], BFlow['TotalPrecip']))
print(sp.stats.spearmanr(BFlow['TotalPrecip'], BFlow['NumDate']))
FPlot1 = floodfreq.plot(x='Decade', y='# of Recorded Floods', kind='bar')

FPlot2 = floodcost.plot(x='Decade', y='Average ETC of Floods (CAD)', kind='bar')
FPlot3 = floodfat.plot(x='Decade', y='Total Fatalities due to Flooding', kind='bar')
FPlot4 = floode.plot(x='Decade', y='Total # of Persons Evacuated due to Flooding', kind='bar')
fig14= FPlot1.get_figure()
fig14.savefig("Fig14.png")
fig15= FPlot2.get_figure()
fig15.savefig("Fig15.png")
fig16= FPlot3.get_figure()
fig16.savefig("Fig16.png")
fig17= FPlot4.get_figure()
fig17.savefig("Fig17.png")
estimator = Ridge()
x=glacier['Mean Yearly Snowfall (mm)']
X=x[:, np.newaxis]
Y=glacier['Mean Yearly Summer Flow (m3/s)']
estimator.fit(X, Y)
xfit = np.array([23])
print(estimator.predict([xfit]))





