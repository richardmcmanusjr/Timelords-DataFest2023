import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.express as px

states_data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/StatePopulations.csv', sep=',', index_col=False)
states_data.rename(columns = {'Population':'ratio'}, inplace = True)
states_data = states_data.set_index('StateAbbr')

data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/questions.csv', sep=',')
data_unanswered = data.loc[data['TakenByAttorneyUno'].isnull()]

data_unanswered['ratio'] = 1

# use groupby() and count() to total up all the tornadoes by state
data_unanswered = data_unanswered[['StateAbbr','ratio']].groupby('StateAbbr').count()

data_unanswered['ratio'] = data_unanswered['ratio']/states_data['ratio']

# sort by most tornadoes first
data_unanswered.sort_values('ratio', ascending=False).head(10)
data_unanswered.rename(columns = {'ratio':'Unanswered Questions/State Population'}, inplace = True)
data_unanswered.to_csv('data.csv')

fig = px.choropleth(data_unanswered,
                    locations='StateAbbr', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Unanswered Questions/State Population',
                    color_continuous_scale="Viridis_r",    
                    )
fig.write_html('first_figure.html', auto_open=True)


