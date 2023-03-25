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

data_unanswered = data.loc[data['TakenByAttorneyUno'].isnull()]

data['Questions'] = 1

data_unanswered['Questions'] = 1

# use groupby() and count() to total up all the tornadoes by state
data = data[['StateAbbr','Questions']].groupby('StateAbbr').count()
data_unanswered = data_unanswered[['StateAbbr','Questions']].groupby('StateAbbr').count()


data_ratio = data_unanswered/data
data_ratio = data_ratio.reset_index()
data_ratio.to_csv('data.csv')

# sort by most tornadoes first
data_ratio.sort_values('Questions', ascending=False).head(10)
data_ratio.rename(columns = {'Questions':'Unanswered Questions/Total Questions'}, inplace = True)

fig = px.choropleth(data_ratio,
                    locations='StateAbbr', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Unanswered Questions/Total Questions',
                    color_continuous_scale="Viridis_r", 
                    
                    )
fig.write_html('first_figure.html', auto_open=True)


