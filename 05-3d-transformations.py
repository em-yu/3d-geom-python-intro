import numpy as np
import polyscope as ps
from scipy.spatial.transform import Rotation as R

ps.init()

# Pyramid
vertices = np.array([
    [1, 0, 0],           # A, vertex 0
    [-0.5, 0, 0.86],     # B, vertex 1
    [-0.5, 0, -0.86],    # C, vertex 2
    [0, 1, 0]            # D, vertex 3
])
faces = np.array([
    [0, 1, 2],
    [0, 1, 3],
    [1, 2, 3],
    [2, 0, 3],
])

ps.register_surface_mesh("pyramid (initial)", vertices, faces)

# ==========================================================================
# 05-A. The goal: translate the pyramid by an offset vector
offset_vector = np.array([2.5, 0, 0])

# vertices_offset = ...

# ps.register_surface_mesh("pyramid (translated)", vertices_offset, faces)

# ==========================================================================
# 05-B. The goal: scale the pyramid
scale_factor = 1.5
offset_vector = np.array([0, 2.5, 0])

# vertices_scaled = ...
# vertices_scaled += offset_vector

# ps.register_surface_mesh("pyramid (scaled)", vertices_scaled, faces)

# ==========================================================================
# 05-C. The goal: rotate the pyramid
# Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html
rotation = R.from_euler('z', 30, degrees=True)
offset_vector = np.array([2.5, 2.5, 0])

# vertices_rotated = rotation.apply(vertices)
# vertices_rotated += offset_vector

# ps.register_surface_mesh("pyramid (rotated)", vertices_rotated, faces)

ps.show()