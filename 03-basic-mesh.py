import numpy as np
import polyscope as ps

# Reference: https://polyscope.run/py/structures/surface_mesh/basics/

# Initialize polyscope 3D viewer
ps.init()

# ==========================================================================
# 03-A. The goal: create a triangle face
# - a triangle has 3 vertices (A, B, C) => create them
vertices = np.array([
    [0, 0, 0],         # A, vertex 0
    [1, 0, 0],         # B, vertex 1
    [0.5, 0.5, 0],     # C, vertex 2
])

# Display the vertices
ps.register_point_cloud("triangle vertices", vertices)

# - a triangle has 1 face = (A, B, C)
# faces = np.array([
#     ...
# ])

# ps.register_surface_mesh("triangle", vertices, faces)

# ==========================================================================
# 03-B. The goal: create a square face
# C -- D
# |    |
# A -- B
# - a square has 4 vertices (A, B, C, D) => create them
vertices = np.array([
    [0, 0, 0],         # A, vertex 0
    [1, 0, 0],         # B, vertex 1
    [0, 1, 0],         # C, vertex 2
    [1, 1, 0],         # D, vertex 3
])

# Display the vertices
ps.register_point_cloud("square vertices", vertices)

# - a square has 1 face = (A, B, D, C) => we give the vertices in counter-clockwise order
# faces = np.array([
#     ...
# ])

# ps.register_surface_mesh("square", vertices, faces)


# ==========================================================================
# 03-C. The goal: create a pyramid with 4 vertices and 4 faces
# - vertices
vertices = np.array([
    [1, 0, 0],           # A, vertex 0
    [-0.5, 0, 0.86],     # B, vertex 1
    [-0.5, 0, -0.86],    # C, vertex 2
    [0, 1, 0]            # D, vertex 3
])
ps.register_point_cloud("pyramid vertices", vertices)

# Faces are: [A, B, C] ; [..., ..., ...] ; [..., ..., ...] ; [..., ..., ...]
# faces = np.array([
#     [0, 1, 2],
#     ...,
#     ...,
#     ...,
# ])

# ps.register_surface_mesh("pyramid", vertices, faces)

ps.show()