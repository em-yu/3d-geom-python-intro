import numpy as np
import polyscope as ps

# Reference: https://polyscope.run/py/structures/point_cloud/basics/

# Initialize polyscope 3D viewer
ps.init()

# ==========================================================================
# 02-A. The goal: create a line of N points along the X axis
pts_A = np.empty((0, 3))
N = 10
# The points coordinates will look like: [x, 0, 0] with x increasing regularly
# for i in range(N):
    # the coordinates of the i-th point
    # pt_i = np.array([...])

    # add it to the list of all points
    # pts_A = np.row_stack([pts_A, pt_i])

ps.register_point_cloud("pts along X", pts_A)

# ==========================================================================
# 02-B. The goal: create a line of points along the Y axis
# The points coordinates will look like: [0, y, 0] with y increasing regularly
# ...

# ps.register_point_cloud("pts along Y", pts_B)


# ==========================================================================
# 02-C. The goal: create a grid of points!

# pts = np.empty((0, 3))

# ...

# ps.register_point_cloud("grid pts", pts)

# Display polyscope viewer window
ps.show()