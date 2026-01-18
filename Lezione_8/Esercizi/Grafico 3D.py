import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = np.array([
    [80, 3],
    [100, 3],
    [120, 4],
    [150, 4],
    [200, 5]
])

y = np.array([180000, 220000, 260000, 320000, 400000])

model = LinearRegression()
model.fit(X, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:,0], X[:,1], y, color='blue')

x_surf = np.linspace(80, 200, 10)
y_surf = np.linspace(3, 5, 10)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = model.predict(np.c_[x_surf.ravel(), y_surf.ravel()]).reshape(x_surf.shape)

ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.4)

ax.set_xlabel("Superficie (m²)")
ax.set_ylabel("Stanze")
ax.set_zlabel("Prezzo (€)")

plt.show()