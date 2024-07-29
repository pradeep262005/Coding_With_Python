import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io import shapereader
from mpl_toolkits.basemap import Basemap
plt.figure(figsize=(5,5))
projection=ccrs.Orthographic(central_longitude=50,central_latitude=0)
m=Basemap()
ax=plt.axes(projection=projection)
m.drawrivers()
ax.coastlines()
ax.set_title('River Projection')
plt.show()
