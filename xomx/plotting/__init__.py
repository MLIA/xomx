from .basic_plot import (
    extension,
    scatter,
    plot,
    plot_scores,
    plot_var,
    plot_2d_obsm,
    plot_2d_embedding,
)

import matplotlib.pyplot as plt

# custom modification to the nipy_spectral colormap
nipy_spectral_colormap = plt.get_cmap("nipy_spectral")
nipy_spectral_colormap._segmentdata["red"][-1] = (1.0, 1.0, 1.0)
nipy_spectral_colormap._segmentdata["green"][-1] = (1.0, 0.0, 0.0)
nipy_spectral_colormap._segmentdata["blue"][-1] = (1.0, 0.0, 0.0)
nipy_spectral_colormap._init()
