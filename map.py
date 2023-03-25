import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.graph_objects as go

nomi = pgeocode.Nominatim('us')

edf = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/clients_1000.csv',
    sep=',',header=None, index_col=False ,names=['Id','StateAbbr','ClientUno','County','StateName',
    'PostalCode','EthnicIdentity','Age','Gender','MaritalStatus','Veteran',
    'Imprisoned','NumberInHousehold','AnnualIncome','AllowedIncome','CheckingBalance',
    'SavingsBalance','InvestmentsBalance','CreatedUtc'
])
edf['Latitude'] = (nomi.query_postal_code(edf['PostalCode'].tolist()).latitude)
edf['Longitude'] = (nomi.query_postal_code(edf['PostalCode'].tolist()).longitude)

fig = go.Figure(data=go.Scattergeo(
        lon = edf['Longitude'],
        lat = edf['Latitude'],
        mode = 'markers',
        ))

fig.update_layout(
        title = 'Distribution',
        geo_scope='usa',
    )
fig.show()