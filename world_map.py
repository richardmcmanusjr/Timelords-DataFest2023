import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()

nomi = pgeocode.Nominatim('us')


edf = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/clients.csv',
    sep=',',header=None, index_col=False ,names=['Id','StateAbbr','ClientUno','County','StateName',
    'PostalCode','EthnicIdentity','Age','Gender','MaritalStatus','Veteran',
    'Imprisoned','NumberInHousehold','AnnualIncome','AllowedIncome','CheckingBalance',
    'SavingsBalance','InvestmentsBalance','CreatedUtc'
])

edf = edf.loc[edf['EthnicIdentity'] == 'African American']

edf['Latitude'] = (nomi.query_postal_code(edf['PostalCode'].tolist()).latitude)
edf['Longitude'] = (nomi.query_postal_code(edf['PostalCode'].tolist()).longitude)

geometry = [Point(xy) for xy in zip(edf['Longitude'], edf['Latitude'])]
gdf = GeoDataFrame(edf, geometry=geometry)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(20, 12)), marker='o', color='red', markersize=15);
plt.savefig('world.jpg')