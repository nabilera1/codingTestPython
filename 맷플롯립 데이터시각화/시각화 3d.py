from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def DCM_ode(state, t):
    w1 = 0.1 * np.sin(2 * t)
    w2 = 0.01 * np.cos(0.2 * t)
    w3 = -0.1 * np.sin(0.1 * t + 0.5)

    wx = np.array([[0, -w3, w2],
                   [w3, 0, -w1],
                   [-w2, w1, 0]])

    DCM = state.reshape(3, 3)

    dDCM_dt = -np.dot(wx, DCM)

    f = dDCM_dt.reshape(9)
    return f


# set box geometry
half_width = 0.3 / 2
half_height = 0.1 / 2
half_depth = 0.1 / 2

# construct box
num_points = 100
num_template = np.linspace(-1, 1, num_points)
x1 = num_template * half_width
y1 = np.ones(num_points) * half_depth
z1 = np.ones(num_points) * half_height

X1 = np.hstack((x1, x1, x1, x1))
Y1 = np.hstack((y1, y1, -y1, -y1))
Z1 = np.hstack((z1, -z1, z1, -z1))
XYZ1 = np.vstack((X1, Y1, Z1))

x2 = np.ones(num_points) * half_width
y2 = num_template * half_depth
z2 = np.ones(num_points) * half_height

X2 = np.hstack((x2, x2, -x2, -x2))
Y2 = np.hstack((y2, y2, y2, y2))
Z2 = np.hstack((z2, -z2, z2, -z2))
XYZ2 = np.vstack((X2, Y2, Z2))

x3 = np.ones(num_points) * half_width
y3 = np.ones(num_points) * half_depth
z3 = num_template * half_height

X3 = np.hstack((x3, x3, -x3, -x3))
Y3 = np.hstack((y3, -y3, y3, -y3))
Z3 = np.hstack((z3, z3, z3, z3))
XYZ3 = np.vstack((X3, Y3, Z3))

# prepare 3D plot
plt.ion()

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

# construct random DCM
b1 = np.random.randn(3)
b2 = np.array([1, 1, -(b1[0] + b1[1]) / b1[2]])
b3 = np.cross(b1, b2)

b1 = b1 / np.sqrt(np.sum(b1 ** 2))
b2 = b2 / np.sqrt(np.sum(b2 ** 2))
b3 = b3 / np.sqrt(np.sum(b3 ** 2))

DCM = np.vstack((b1, b2, b3))
DCM = DCM.T
DCM = np.eye(3)

# generate time points
num_time = 100
time_all = np.linspace(0, 2, num_time)

# run loop
for tidx in range(0, num_time - 1):
    print(tidx)
    XYZ1 = np.dot(DCM.T, XYZ1)
    XYZ2 = np.dot(DCM.T, XYZ2)
    XYZ3 = np.dot(DCM.T, XYZ3)
    ax.plot(XYZ1[0], XYZ1[1], XYZ1[2], 'b.')
    ax.plot(XYZ2[0], XYZ2[1], XYZ2[2], 'r.')
    ax.plot(XYZ3[0], XYZ3[1], XYZ3[2], 'g.')

    ax.view_init(30, 30)
    ax.set_xlim3d(-0.5, 0.5)
    ax.set_ylim3d(-0.5, 0.5)
    ax.set_zlim3d(-0.5, 0.5)

    plt.draw()
    plt.pause(0.01)
    ax.clear()

    ic = DCM.reshape(9)
    t0 = time_all[tidx]
    tf = time_all[tidx + 1]
    t_all = np.linspace(t0, tf, 100)
    y_all = odeint(DCM_ode, ic, t_all)
    DCM = y_all[-1].reshape(3, 3)