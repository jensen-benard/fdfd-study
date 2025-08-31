from pint import UnitRegistry
import numpy as np
import matplotlib.pyplot as plt

ureg = UnitRegistry()

# DASHBOARD

GRID_SIZE_X = 1
GRID_SIZE_Y = 1

CELL_COUNT_X = 100
CELL_COUNT_Y = 100

x0 = 0.3
y0 = 0.6
rx = 0.2
ry = 0.35
angle = 30 * ureg.degree

# CALCULATION

cellSizeX = GRID_SIZE_X / CELL_COUNT_X
cellSizeY = GRID_SIZE_Y / CELL_COUNT_Y

axisX = np.arange(0.5, CELL_COUNT_X - 0.5 + 1) * cellSizeX
axisY = np.arange(0.5, CELL_COUNT_Y - 0.5 +1) * cellSizeY

meshGridY, meshGridX = np.meshgrid(axisY, axisX, indexing='ij')

# Rotate the meshgrid
thetas = np.angle((meshGridX - x0) + (meshGridY - y0)*1j)
r =  np.abs((meshGridX - x0) + (meshGridY - y0)*1j)

meshGridX = r * np.cos(thetas + angle) + x0
meshGridY = r * np.sin(thetas + angle) + y0

relativePermeabilityGrid = ((meshGridX - x0)/rx)**2 + ((meshGridY - y0)/ry)**2 <= 1


# PLOT
plt.imshow(relativePermeabilityGrid, extent=[0, GRID_SIZE_X, GRID_SIZE_Y, 0], cmap='gray')

plt.show()