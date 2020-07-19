
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


# threebody with matplotlib
# didn't see anything wrong but not working
# in my idea is that the time between each frame is too large


def updatePosition(num,position,speed):
    global scats
    for scat in scats:
        scat.remove()
    scats=[]
    scats.append(ax.scatter(position[0][0],position[0][1],position[0][2], c = 'b'))
    scats.append(ax.scatter(position[1][0],position[1][1],position[1][2], c = 'r'))
    scats.append(ax.scatter(position[2][0],position[2][1],position[2][2], c = 'y'))
    a1,a2,a3 = newtonGravity(weight1,weight2,weight3,position)
    speed[0] = speed[0] + a1
    speed[1] = speed[1] + a2
    speed[2] = speed[2] + a3
    position[0] = position[0] + speed[0]/4
    position[1] = position[1] + speed[1]/4
    position[2] = position[2] + speed[2]/4
    # print(position)


def vector(pos1,pos2):
    d = pos2-pos1
    
    if np.sum(np.absolute(d)) < 1.5:
        return 0
    else:
        return d/np.absolute(d)
    
def newtonGravity(m1,m2,m3,pos):
    G = 6.754*10**-11  #N·m²/kg²
    f12 = (G*m1*m2)/np.sum((pos[0]-pos[1])**2)*vector(pos[0],pos[1])
    f13 = (G*m1*m3)/np.sum((pos[0]-pos[2])**2)*vector(pos[0],pos[2])
    f1= f12 + f13

    # print(np.absolute(f1))

    f21 = -f12
    f23 = (G*m2*m3)/np.sum((pos[1]-pos[2])**2)*vector(pos[1],pos[2])
    f2 = f21 + f23

    f31 = -f13
    f32 = -f23
    f3 = f31 + f32


    a1 = f1/m1
    a2 = f2/m2
    a3 = f3/m3
    # print(a1)
    # print(a2)
    # print(a3)
    return a1,a2,a3



# Attaching 3D axis to the figure
scats = []
fig = plt.figure()
ax = p3.Axes3D(fig)
weight1 = 100**4
weight2 = 100**4
weight3 = 100**4
speed = np.zeros((3,3))
position = np.random.rand(3,3)*10


ax.set_xlim3d([-10, 10])
ax.set_xlabel('X')

ax.set_ylim3d([-10, 10])
ax.set_ylabel('Y')

ax.set_zlim3d([-10, 10])
ax.set_zlabel('Z')

ax.set_title('3D Test')
pp = [[1,1,1],[1,2,1],[1,1,3]]
pp = np.array(pp)
newtonGravity(weight1,weight2,weight3,pp)


# # Creating the Animation object
line_ani = animation.FuncAnimation(fig, updatePosition,  fargs = (position,speed),
                                   interval=5, blit=False)

plt.show()
