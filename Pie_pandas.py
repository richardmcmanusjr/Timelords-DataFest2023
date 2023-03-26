import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.express as px

data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/questions.csv', sep=',')
data = data.loc[data['TakenByAttorneyUno'].isnull()]

category = 'StateAbbr'
valueName = 'ME'

subCategory = 'Category'
subValueName = None #'Family and Children'

if valueName != None:
    data = data.loc[data[category] == valueName]

newCol = 'Categories'

data[newCol] = 1

# use groupby() and count() to total up all the tornadoes by state
data = data[['Category',newCol]].groupby('Category').count()

# sort by most first
data = data.sort_values(newCol, ascending=False)
data.to_csv('data_un.csv')

colors = ['#3E0751', '#43838B', '#5CB180', '#5CB180', '#B8DC53', '#D7E153', '#EFE554', '#F9E855', '#F9E855', '#F9E855' ]

data.plot.pie(y=newCol, labels=None, figsize=(12, 6), title='Categories of Unanswered Questions (Maine)',
    wedgeprops = { 'linewidth' : 0.5, 'edgecolor' : 'white' }, colors=colors)
plt.legend(labels=data.index, bbox_to_anchor=(1, 0.75), loc="upper left")
plt.ylabel("")
plt.show()

