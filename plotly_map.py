import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.express as px

nomi = pgeocode.Nominatim('us')

data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/clients.csv',
    sep=',',header=None, index_col=False ,names=['Id','StateAbbr','ClientUno','County','StateName',
    'PostalCode','EthnicIdentity','Age','Gender','MaritalStatus','Veteran',
    'Imprisoned','NumberInHousehold','AnnualIncome','AllowedIncome','CheckingBalance',
    'SavingsBalance','InvestmentsBalance','CreatedUtc'
])

data = data.loc[data['EthnicIdentity'] == 'African American']

data['Latitude'] = (nomi.query_postal_code(data['PostalCode'].tolist()).latitude)
data['Longitude'] = (nomi.query_postal_code(data['PostalCode'].tolist()).longitude)
data.to_csv('data.csv')

fig = px.scatter_mapbox(data, lat="Latitude", lon="Longitude", hover_name="ClientUno", hover_data=["EthnicIdentity", "Age"],
    color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html('first_figure.html', auto_open=True)


