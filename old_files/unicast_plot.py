import random
from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d, art3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


lines = [(2, 2), (+0.00, 16), (14.0, 14.0), 2.0, '#5600fa'],\
        [(8, 8), (-0.25, 16), (8.00, 8.00), 2.0, '#4400c7'],\
        [(2, 2), (+0.00, 16), (2.00, 2.00), 2.0, '#20005e']

points = [[[1, 1.00], [3, 2.00], '#ffaf24'],
          [[2, 1.00], [3, 3.00], '#00d990'],
          [[1, 2.00], [3, 4.00], '#e9ed00'],
          [[3, 5.00], [1, 6.00], '#f00a4f'],
          [[1, 7.00], [2, 8.00], '#7744c9']]

def plot_process(arrow):
    xz = {1:[2,14],2:[8,8],3:[2,2]}
    x1, z1, y1, x2, z2, y2, arrow_color, box = xz[arrow[0][0]] + [
        2*arrow[0][1]] + xz[arrow[1][0]] + [2*arrow[1][1]] + [arrow[2]] + [{'alpha': 0.1, 'pad': 1}]
    ax.scatter(x1, y1, z1, color='black', marker='s')
    ax.scatter(x2, y2, z2, color='green', marker='s')
    ax.add_artist(Arrow3D((x1, x2), (y1, y2), (z1, z2),
                          mutation_scale=10, lw=1.5, arrowstyle="-|>", color=arrow_color))
    if z1 > z2:
        ax.text(x1, y1+0.00, z1+0.5, int(y1/2), size=10,  zorder=1, color='#ff0000', bbox=box)
        ax.text(x2, y2-0.25, z2-1.0, int(y2/2), size=10,  zorder=1, color='#49a800', bbox=box)
    else:
        ax.text(x1, y1-0.25, z1-1.0, int(y1/2), size=10,  zorder=1, color='#ff0000', bbox=box)
        ax.text(x2, y2-0.25, z2+0.5, int(y2/2), size=10,  zorder=1, color='#49a800', bbox=box)
    ax.text((x1+x2)*0.5, (y1+y2)*0.5 + 0.225, (z1+z2)*0.5,
            int(y1/2), size=10, zorder=1, color='#ff7b08', bbox=box)

def rotation_view(ax, plt):
    for angle in range(0, 360):
        ax.view_init(17, angle)
        plt.draw()
        plt.pause(.01)


fig = plt.figure()
fig.set_size_inches(15, 15)
ax = fig.add_subplot(111, projection='3d', aspect='equal')

ax.view_init(azim=17, elev=17)
ax.grid(False)

ax.set_xlim(16, 0)
ax.set_ylim(0, 16)
ax.set_zlim(0, 16)

ax.set_xticklabels('')
ax.set_ylabel('Time')
ax.set_yticklabels(list(range(0, 9)))
ax.set_zticklabels(['', 'P_3', '', '', 'P_2', '', '', 'P_1'])

ax.set_title('Lamport\'s Clocks (Unicast System)', fontsize=16)

for line in lines:
    x1x2, y1y2, z1z2, line_width, color = line
    ax.add_line(art3d.Line3D(x1x2, y1y2, z1z2, lw=line_width, color=color))
    ax.text(x1x2[0], y1y2[0], z1z2[0]+0.5, 0, size=10, zorder=1,
            color='black', bbox={'alpha': 0.1, 'pad': 1})

for arrow in points:
    plot_process(arrow)

plt.show()
# rotation_view(ax,plt)

'''def r(): return random.randint(0, 255)
print('#%02X%02X%02X' % (r(), r(), r()))
colors = ['#1b1b1e', '#373f52', '#55a4b1', '#a8bcd1', '#d8dbe2', '#976fac', '#6dc3ba', '#b58ca3', '#8f6c7d', '#c8b9fe', '#b6a092', '#716a5a', '#420420', '#dfa61f', '#28140c', '#411010', '#004c00', '#3c1515', '#ff7f24', '#ff0000', '#ff00ff',
          '#413413', '#612612', '#4bec13', '#b58ca3', '#6c7d8f', '#8f6c7d', '#c8b9fe', '#9eeac1', '#98f019', '#3cceda', '#e23425', '#000000', '#4c4c4c', '#e5e5e5', '#6d0c24', '#ff4982', '#6897bb', '#fff68f', '#b0e0e6', '#f7347a', '#4f97a3']'''
