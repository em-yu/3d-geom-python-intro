import numpy as np
import polyscope as ps

# Reference: https://polyscope.run/py/structures/surface_mesh/basics/

# Initialize polyscope 3D viewer
ps.init()
# ==========================================================================
# 04-A. The goal: create a 2x2 grid of faces
# G -- H -- I
# |    |    |
# D -- E -- F
# |    |    |
# A -- B -- C
A = np.array([0, 0, 0]) # index 0
B = np.array([1, 0, 0]) # index 1
C = np.array([2, 0, 0]) # index 2
D = np.array([0, 1, 0]) # index 3
E = np.array([1, 1, 0]) # index 4
F = np.array([2, 1, 0]) # index 5
G = np.array([0, 2, 0]) # index 6
H = np.array([1, 2, 0]) # index 7
I = np.array([2, 2, 0]) # index 8

vertices_2x2 = np.array([A, B, C, D, E, F, G, H, I])
# display vertices and inspect them
ps.register_point_cloud("vertices 2x2", vertices_2x2)

face_ABED = np.array([0, 1, 4, 3])
# face_BCFE = ...

# faces_2x2 = np.array([face_ABED, ...])

# ps.register_surface_mesh("2x2 mesh", vertices_2x2, faces_2x2)

# ==========================================================================
# 04-B. The goal: adapt code from 02-C to create not only the points but also the faces
# pts = np.empty((0, 3))

pts = np.empty((0, 3), dtype=float)
faces = np.empty((0, 4), dtype=int) # Faces are composed of vertex indices, so the values are integers
N_x = 8
N_y = 10
# Create all vertices
for j in range(N_y):
    for i in range(N_x):
        pts = np.row_stack([
            pts,
            np.array([i, j, 0])
        ])
# Create all faces
# for j in range(N_y - 1):
#     for i in range(N_x - 1):
        # C -- D
        # |    |
        # A -- B
        # A = ...
        # B = ...
        # C = ...
        # D = ...
        # face = np.array([A, B, D, C])

        # faces = np.row_stack([faces, face])

ps.register_point_cloud("grid pts", pts)
ps.register_surface_mesh("grid mesh", pts, faces)

# ==========================================================================
# 04-C. The goal: change the Z-value of the points by replacing them with random values
pts_with_noise = np.array(pts) # copy grid vertices

random_x = np.random.rand(len(pts_with_noise))

# Change the whole column (z-coordinate for all points)
pts_with_noise[:, 2] = random_x

ps.register_surface_mesh("grid mesh (with noise)", pts_with_noise, faces)


ps.show()