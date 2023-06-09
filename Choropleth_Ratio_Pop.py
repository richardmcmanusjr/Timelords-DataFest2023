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
states_data = states_data.sort_index()
states_data.to_csv('states.csv')
data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/questions.csv', sep=',')
data = data.loc[data['StateAbbr'] != 'ID']
data = data.loc[data['StateAbbr'] != 'US']

data['ratio'] = 1

# use groupby() and count() to total up all the tornadoes by state
data = data[['StateAbbr','ratio']].groupby('StateAbbr').count()
data = data.sort_index()
data.to_csv('data.csv')

data_list = data['ratio'].tolist()
states_data_list = states_data['ratio'].tolist()
data_ratio_list = []

for i in range (len(data_list)):
    data_ratio_list.append(data_list[i]/states_data_list[i])

data_ratio = data
data_ratio['ratio'] = data_ratio_list

# sort by most tornadoes first
data_ratio = data_ratio.sort_values('ratio', ascending=False)
data_ratio = data_ratio.reset_index()
data_ratio.rename(columns = {'ratio':'Total Questions/Population per Million'}, inplace = True)

fig = px.choropleth(data_ratio,
                    locations='StateAbbr', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Total Questions/Population per Million',
                    color_continuous_scale="Viridis_r",    
                    )
fig.write_html('first_figure.html', auto_open=True)


