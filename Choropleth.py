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

category = 'TakenByAttorneyUno'
valueName = 'Unanswered Questions'

subCategory = 'Category'
subValueName = None

if valueName == 'Unanswered Questions':
    data = data.loc[data[category].isnull()]

elif valueName != None:
    data = data.Loc[data[category] == valueName]

if subValueName != None:
    data = data.loc[data[subCategory] == subValueName]

# Add a new column and set the value to 1
if subValueName != None:
    newCol = valueName + ' about ' + subValueName

elif valueName != None:
    newCol = valueName

else:
    newCol = 'Questions Asked'

data[newCol] = 1

# use groupby() and count() to total up all the tornadoes by state
data = data[['StateAbbr',newCol]].groupby('StateAbbr').count().reset_index()

# sort by most tornadoes first
data.sort_values(newCol, ascending=False).head(10)

fig = px.choropleth(data,
                    locations='StateAbbr', 
                    locationmode="USA-states", 
                    scope="usa",
                    color=newCol,
                    color_continuous_scale="Viridis_r", 
                    
                    )
fig.write_html('first_figure.html', auto_open=True)


