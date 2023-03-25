import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.express as px
    

fig1 = plt.figure() 
ax = fig1.add_subplot()

ax.set_xlim(-130.00, -62.50000)
ax.set_ylim(20.00000, 55.50000)

nomi = pgeocode.Nominatim('us')

data = pd.read_csv('/Users/richardmcmanjus/Documents/College/Datafest/Data/clients.csv',
    sep=',',header=None, index_col=False ,names=['Id','StateAbbr','ClientUno','County','StateName',
    'PostalCode','EthnicIdentity','Age','Gender','MaritalStatus','Veteran',
    'Imprisoned','NumberInHousehold','AnnualIncome','AllowedIncome','CheckingBalance',
    'SavingsBalance','InvestmentsBalance','CreatedUtc'
])

#category = 'Not Hispanic or Latino'

#data = data.loc[data['EthnicIdentity'] == category]
postalCodes = data['PostalCode'].tolist()
print(len(postalCodes))
Latitude = []
Longitude = []
for i in range(len(postalCodes)):
    if i % 1000 == 0:
        print(i)
    try:
        Latitude.append(nomi.query_postal_code(postalCodes[i]).latitude)
        Longitude.append(nomi.query_postal_code(postalCodes[i]).longitude)
    except:
        Latitude.append(None)
        Longitude.append(None)

data['Latitude'] = Latitude
data['Longitude'] = Longitude
data.to_csv('data.csv')

geometry = [Point(xy) for xy in zip(data['Longitude'], data['Latitude'])]
gdf = GeoDataFrame(data, geometry=geometry, crs="EPSG:3395")

states = gpd.read_file('geopandas-tutorial-master/data/usa-states-census-2014.shp', crs="EPSG:3395")
states.boundary.plot(ax=ax, color='black', linewidth=.8)
gdf.plot(ax=ax, color='red', marker='o', markersize=8)


# Create a copy of the original DataFrame
ethnicity_by_state = data.copy()
# Add a new column and set the value to 1
ethnicity_by_state[category] = 1

# use groupby() and count() to total up all the tornadoes by state
ethnicity_by_state = ethnicity_by_state[['StateAbbr',category]].groupby('StateAbbr').count()

# sort by most tornadoes first
ethnicity_by_state.sort_values(category, ascending=False).head(10)

ethnicity_by_state.to_csv('ethnicity_by_state.csv')

ethnicity_by_state.plot.bar(figsize=(12,6), title='African Americans by State')

plt.show()