import numpy as np
import polyscope as ps

# Reference: https://polyscope.run/py/structures/point_cloud/basics/

# Initialize polyscope 3D viewer
ps.init()

# ==============================================
# 01-A. The goal: display one 3D point
pt_x = 0
pt_y = 0
pt_z = 0

# We represent the 3D point by a numpy array: [pt_x, pt_y, pt_z]
# pt = np.array([pt_x, pt_y, pt_z])

# inspect the point in the console:
# print(pt)

# A point cloud is a list of 3D points, so it must have a shape like (N, 3)
# where N is the number of points
# Here N = 1, so the shape should be (1, 3)
# pt_cloud_shape = (1, 3)
# pt_cloud = pt.reshape(pt_cloud_shape)

# ps.register_point_cloud("3D point", pt_cloud)

# ==============================================
# 01-B. The goal: display random 3D points

# Generate N random points with numpy
N = 30
# First generate 3 list of random values
pts_x = np.random.random_sample(N)
pts_y = np.random.random_sample(N)
pts_z = np.random.random_sample(N)

# We build the point cloud by assembling the 3 lists
# column_stack assembles the lists vertically
pts = np.column_stack([
    pts_x, pts_y, pts_z
])

# inspect the points coordinates in the console:
# print(pts)

# ps.register_point_cloud("Random points", pts)

# ==============================================
# 01-C. The goal: display values on the points
# Ref: https://polyscope.run/py/structures/point_cloud/scalar_quantities/

# arange(N) creates an array with N elements like: [0 1 2 3 ... N-1]
# pts_weight = np.arange(N)

# We keep a reference to our point cloud object that we name "ps_random_pts"
# ps_random_pts = ps.register_point_cloud("Random points", pts)
# Using "add_scalar_quantity" method, we display the weights on the points
# ps_random_pts.add_scalar_quantity("weight", pts_weight)

# Display polyscope viewer window
ps.show()