import pandas as pd
import matplotlib.pyplot as pl
df=pd.read_csv(r"C:\Users\PRADEEP\Desktop\FDS\22102040-UCI Diabetics2.csv")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(0, 5, 20)
xline = df['Age'].head(20)
yline = df['Itching'].head(20)
ax.scatter3D(xline, yline, zline, 'greenmaps')
plt.show()

