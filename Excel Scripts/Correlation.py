import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
import scipy.stats as stats
import matplotlib.mlab as mlab
import pylab as pl
from PIL import Image


df1= pd.read_csv('C:/users/sreitz/Downloads/Hours Spent.csv', encoding='latin1')
description= df1.corr(method='pearson')
print(description)



# mu= df1.std()
# variance= df1.var()
# sigma=np.sqrt(variance)
# x=np.linspace(mu.all()-3*sigma.all(),mu.all()+3*sigma.all(),100)
# description=plt.plot(x,mlab.normpdf(x,mu,sigma))
fit=stats.norm.pdf(df1,np.mean(df1),np.std(df1))
one=pl.plot(df1,fit,'-o')
two=pl.hist(df1, normed=True)
pl.show()
one.savefig("F:/Steve/tdsa.png")


print(df1.skew())
print(df1.kurt())
fig= description.get_figure()
fig.savefig('F:/Steve/Test Correlation.png')
#im=Image.fromarray(description)
#im.save('F:/Steve/Windows Test.png')
fig=sns.lmplot(x='Sc'Hours Spent',data=df1,fit_reg=True) 
fig.savefig('F:/Steve/Line Correlation.png')

#description.to_csv('F:/Steve/PPEP F18 Average Score w 0s Described.csv', encoding='latin1')ore',y=