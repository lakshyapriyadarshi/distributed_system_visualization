'''from unicast_user1 import perform
messages = []
print("ENTER COMMAND")
while(1):
        print('in while')
        command = input()
        print('took command')
        if command == 'end':
                print('took end')
                break
        else:
                if 'add' in command:
                        print('took add')
                        adder = str(command[command.find('(')+1:command.find(')')])
                        print('adder',adder)
                        message = list(map(int, adder.split(sep=',')))
                        print('message', message)
                        messages.append(message)
                        print('messages')
                        print(*messages, sep = '\n')
                elif 'del' in command:
                        deleter = int(
                            command[command.find('(')+1:command.find(')')])
                        del messages[int(deleter)]
                print('calling perform')
                perform(messages)
                print('returned from perform')'''

from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d, art3d
import random
from scipy import eye
fig = plt.figure(figsize=(50, 50))
ax = fig.add_subplot(111, projection='3d', aspect='equal')
plt.show()
# p.imshow(eye(3))
plt.show()
print ('a')
# p.imshow(eye(6))
plt.show()
print ('b')
# p.imshow(eye(9))
plt.show()
print ('c')
