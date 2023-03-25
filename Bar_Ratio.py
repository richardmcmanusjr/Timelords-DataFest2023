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

data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/questions.csv', sep=',')

data_unanswered = data.loc[data['TakenByAttorneyUno'].isnull()]

data['Questions'] = 1

data_unanswered['Questions'] = 1

# use groupby() and count() to total up all the tornadoes by state
data = data[['StateAbbr','Questions']].groupby('StateAbbr').count()
data_unanswered = data_unanswered[['StateAbbr','Questions']].groupby('StateAbbr').count()


data_ratio = data_unanswered/data
data_ratio.to_csv('data.csv')

# sort by most tornadoes first
data_ratio = data_ratio.sort_values('Questions', ascending=False)
data_ratio.rename(columns = {'Questions':'Unanswered Questions/Total Questions'}, inplace = True)

data_ratio.plot.bar(figsize=(12,6), title='Unanswered Questions/Total Questions by State')

plt.show()

