from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d, art3d
import random
from display_status import status_report_multicast, information

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

def print_list(data):
    print(" ".join(str(element) for element in data))

def initialize_plot(axis):
        axis.view_init(azim=17, elev=17)
        axis.grid(False)
        axis.set_xlim(limit, 0)
        axis.set_ylim(0, limit)
        axis.set_zlim(0, limit)
        axis.set_xticklabels('')
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        axis.set_yticks(list(range(0, 16)))
        axis.set_ylabel('Time')
        axis.set_xlabel('')
        axis.set_zlabel('')
        axis.set_title('Lamport\'s Clock (Multicast System)', fontsize=16)
        return axis

def plot_lines(lines):
        for line in lines:
            line_width = 2.0
            x1x2, y1y2, z1z2, color = line
            ax.add_line(art3d.Line3D(x1x2, y1y2, z1z2, lw=line_width, color=color))
            text_args = {'size' : 10, 'zorder' : 1, 'bbox' : box}
            ax.text(x1x2[0], y1y2[0], z1z2[0]+0.5, '0', color='black', **text_args)

def plot_message(arrow):
    plt.ion()
    x0, z0 = xz[arrow[0]]
    x1, z1 = xz[arrow[1]]
    x2, z2 = xz[arrow[2]]
    y0, y1, y2 = arrow[3], arrow[4], arrow[5]
    box = {'alpha': 0.1, 'pad': 1}
    arrow_color = random.choice(color_list)
    xt1, yt1, zt1 = (x0+x1)/2, (y0+y1)/2 + 0.225, (z0+z1)/2
    xt2, yt2, zt2 = (x0+x2)/2, (y0+y2)/2 + 0.225, (z0+z2)/2
    text_args = {'size' : 10, 'zorder' : 1, 'bbox' : box}
    arrow_args = {'mutation_scale' : 10, 'lw' : 1.5, 'arrowstyle' : "-|>" , 'color' : arrow_color}
    ax.scatter(x0, y0, z0, color='black', marker='s')
    ax.scatter(x1, y1, z1, color='green', marker='s')
    ax.scatter(x2, y2, z2, color='green', marker='s')
    ax.add_artist(Arrow3D((x0, x1), (y0, y1), (z0, z1), **arrow_args))
    ax.add_artist(Arrow3D((x0, x2), (y0, y2), (z0, z2), **arrow_args))
    if z0>z1:
            y01,z01,y11,z11 = y0,z0+0.5,y1-0.25,z1-1.0
    else:
            y01,z01,y11,z11 = y0-0.25,z0-1.0,y1-0.25,z1+0.5
    ax.text(x0,  y01, z01, int(y0), color='#ff0000', **text_args)
    ax.text(x1,  y11, z11, int(y1), color='#49a800', **text_args)
    ax.text(xt1, yt1, zt1, int(y0), color='#ff7b08', **text_args)
    if z0 > z2:
            y01, z01, y21, z21 = y0, z0+0.5, y2-0.25, z2-1.0
    else:
            y01, z01, y21, z21 = y0-0.25, z0-1.0, y2-0.25, z2+0.5
    ax.text(x2,  y21, z21, int(y2), color='#49a800', **text_args)
    ax.text(xt2, yt2, zt2, int(y0), color='#ff7b08', **text_args)


def send(message):
    process_a, process_b, process_c, timestamp = message
    initial_time = timestamp if timestamp != None else process_time[process_a-1][-1] + step[process_a-1]
    final_time_b = max(process_time[process_b-1][-1],initial_time) + step[process_b-1]
    final_time_c = max(process_time[process_c-1][-1],initial_time) + step[process_c-1]
    process_time[process_a-1].append(initial_time)
    process_time[process_b-1].append(final_time_b)
    process_time[process_c-1].append(final_time_c)
    data = [process_a, process_b, process_c, initial_time, final_time_b, final_time_c]
    plot_message(data)
    return data


def plot_internal(point):
        x1, z1, y1 = xz[point[0]] + [point[1]]
        text_args = {'size': 10, 'zorder': 1, 'bbox': box}
        ax.scatter(x1, y1, z1, color='black', marker='s')
        ax.text(x1, y1, z1+0.5, y1, color='#ff0000', **text_args)


def internal_event(internal_process):
        process, timestamp = internal_process
        final_time = max(process_time[process-1][-1], timestamp) + step[process-1]
        process_time[process-1].append(final_time)
        plot_internal([process, final_time])
        return [process, 'x', 'x', 'x', final_time]

limit = 16
xz = {1: [2, 14], 2: [8, 8], 3: [2, 2]}
box = {'alpha': 0.1, 'pad': 1}
color_list = open('colors.txt', 'r').read().splitlines()
colors = ['#ffaf24','#00d990','#e9ed00','#f00a4f','# 7744c9']
lines = [[(2, 2), (0, 16), (14.0, 14.0), '#5600fa'],
         [(8, 8), (0, 16), (8.00, 8.00), '#4400c7'],
         [(2, 2), (0, 16), (2.00, 2.00), '#20005e']]

messages = []
internals = []
process_table = []
process_time = [[0] for _ in range(3)]

fig = plt.figure(figsize=(50, 50))
ax = fig.add_subplot(111, projection='3d', aspect='equal')
ax = initialize_plot(ax)
plt.ion()

information()
step = list(map(int, input('ENTER STEP SIZE FOR PROCESS 1 , 2 , 3 :\n').strip().split(sep = ' ')))[:3]
plot_lines(lines)

while(1):
        print('\nADD PROCESS')
        command = input()
        if command == 'end':
                break
        else:
                if 'internal' in command:
                        internal = list(map(int,command.strip().split(sep = ' ')[1:]))
                        internals.append(internal)
                        process_table.append(['INTERNAL',internal_event(internals[-1])])
                elif 'send' in command:
                        message = list(map(int,command.strip().split(sep = ' ')[1:]))
                        messages.append(message)
                        process_table.append(['MESSAGE',send(messages[-1])])
                status_report_multicast(process_table)
                plt.show()
