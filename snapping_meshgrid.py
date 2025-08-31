import numpy as np

gridSizeX = 1
gridSizeY = 1

CRITICAL_DIMENSION_X = 1
CRITICAL_DIMENSION_Y = 1

CELL_RESOLUTION = 1 # Number of cells per smallest wavelength

REFRACTIVE_INDEX_MAX = 1

FREE_SPACE_WAVELENGTH = 1

# Set a cell size based on the smallest wavelength and cell resolution 
cellSizeX = FREE_SPACE_WAVELENGTH / REFRACTIVE_INDEX_MAX / CELL_RESOLUTION
cellSizeY = cellSizeX

# Readjust the cell size to snap to a critical dimension
cellCountXForCritDim = np.ceil(CRITICAL_DIMENSION_X / cellSizeX).astype(int)
cellCountYForCritDim = np.ceil(CRITICAL_DIMENSION_Y / cellSizeY).astype(int)
cellSizeX = CRITICAL_DIMENSION_X / cellCountXForCritDim
cellSizeY = CRITICAL_DIMENSION_Y / cellCountYForCritDim

# Readjusting grid size to snap to critical dimension (using the snapped cell size)
cellCountForGridX = np.ceil(gridSizeX / cellSizeX).astype(int)
cellCountForGridY = np.ceil(gridSizeY / cellSizeY).astype(int)
gridSizeX = cellCountForGridX * cellSizeX
gridSizeY = cellCountForGridY * cellSizeY