from pint import UnitRegistry
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

ureg = UnitRegistry()



# DASHBOARD

# gridSizeX = 1
# gridSizeY = 1

# CRITICAL_DIMENSION_X = 1
# CRITICAL_DIMENSION_Y = 1

# CELL_RESOLUTION = 1 # Number of cells per smallest wavelength

# REFRACTIVE_INDEX_MAX = 1

# FREE_SPACE_WAVELENGTH = 1

# # Set a cell size based on the smallest wavelength and cell resolution 
# cellSizeX = FREE_SPACE_WAVELENGTH / REFRACTIVE_INDEX_MAX / CELL_RESOLUTION
# cellSizeY = cellSizeX

# # Readjust the cell size to snap to a critical dimension
# cellCountXForCritDim = np.ceil(CRITICAL_DIMENSION_X / cellSizeX).astype(int)
# cellCountYForCritDim = np.ceil(CRITICAL_DIMENSION_Y / cellSizeY).astype(int)
# cellSizeX = CRITICAL_DIMENSION_X / cellCountXForCritDim
# cellSizeY = CRITICAL_DIMENSION_Y / cellCountYForCritDim

# # Readjusting grid size to snap to critical dimension (using the snapped cell size)
# cellCountForGridX = np.ceil(gridSizeXX / cellSizeX).astype(int)
# cellCountForGridY = np.ceil(gridSizeY / cellSizeY).astype(int)
# gridSizeX = cellCountForGridX * cellSizeX
# gridSizeY = cellCountForGridY * cellSizeY


GRID_SIZE_X = 1
GRID_SIZE_Y = 1
GRID_SIZE_Z = 3

CELL_COUNT_X = 20
CELL_COUNT_Y = 20
CELL_COUNT_Z = 60

rx = 0.4
ry = 0.3
rz = 1.0

er1 = 1.0
er2 = 9.0

# CALCULATION
cellSizeX = GRID_SIZE_X / CELL_COUNT_X
axisX = np.arange(1, CELL_COUNT_X + 1) * cellSizeX
axisX = axisX - np.mean(axisX)

cellSizeY = GRID_SIZE_Y / CELL_COUNT_Y
axisY = np.arange(1, CELL_COUNT_Y + 1) * cellSizeY
axisY = axisY - np.mean(axisY)

cellSizeZ = GRID_SIZE_Z / CELL_COUNT_Z
axisZ = np.arange(1, CELL_COUNT_Z + 1) * cellSizeZ
axisZ = axisZ - np.mean(axisZ)

meshGridY, meshGridX, meshGridZ = np.meshgrid(axisY, axisX, axisZ, indexing='ij')

relativePermeabilityGrid = (meshGridX/rx)**2 + (meshGridY/ry)**2 + (meshGridZ/rz)**2 < 1
relativePermeabilityGrid = er1 + (er2 - er1) * relativePermeabilityGrid

grid = pv.ImageData()
grid.dimensions = np.array(relativePermeabilityGrid.shape) + 1
grid.cell_data["epsilon_r"] = relativePermeabilityGrid.flatten(order="F")
# Threshold to show only cells with epsilon_r > er1
thresholded = grid.threshold(er2, scalars="epsilon_r")

# Plot
# Scale the grid to match physical dimensions
thresholded.scale([GRID_SIZE_X/CELL_COUNT_X, GRID_SIZE_Y/CELL_COUNT_Y, GRID_SIZE_Z/CELL_COUNT_Z])

# Plot
plotter = pv.Plotter()
plotter.add_mesh(thresholded, show_edges=True, cmap="viridis")

# Add full 3D axes with tick marks
plotter.add_axes()  # interactive=True allows you to rotate the axes

# Add numeric axes with custom ticks
plotter.show_bounds(
    grid='back',          # display axes on back plane
    ticks='outside',      # ticks outside the axes
    bounds=(0, CELL_COUNT_X, 0, CELL_COUNT_Y, 0, CELL_COUNT_Z),
    xlabel='X-axis', ylabel='Y-axis', zlabel='Z-axis',
    font_size=15,
    n_xlabels=5,          # number of X-axis labels
    n_ylabels=5,          # number of Y-axis labels
    n_zlabels=6,          # number of Z-axis labels
    location='outer',
    minor_ticks=True,
    use_3d_text=True      # use 3D text for labels
)

plotter.show()