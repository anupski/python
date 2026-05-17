import matplotlib

print(matplotlib.__version__)

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6,4))
plt.plot(x, y, color='blue', marker='o', linestyle='--', label='y = 2x')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]       
y2 = [1, 8, 27, 64, 125]     
y3 = [2, 4, 6, 8, 10]        

plt.figure(figsize=(8,6))


plt.plot(x, y1, color='red', marker='o', linestyle='-', label='y = x²')
plt.plot(x, y2, color='green', marker='s', linestyle='--', label='y = x³')
plt.plot(x, y3, color='blue', marker='^', linestyle='-.', label='y = 2x')


plt.title("Multiple Line Plots Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.legend()
plt.grid(True)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

size = [20, 30, 40]
labels = ['apple', 'banana', 'cherry']
plt.figure(figsize=(6,6))
plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()

#----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']


explode = [0.05 if s < max(sizes) else 0.15 for s in sizes]

fig, ax = plt.subplots(figsize=(6,6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,  
    wedgeprops={'edgecolor':'white','linewidth':1},
    textprops={'fontsize':12}
)


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

ax.set_title("Fruit Distribution", fontsize=16, weight='bold')
ax.axis('equal')  

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4, 8, 1, 10])

plt.plot(xpoints, ls = ':')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4, 8, 1, 10])

plt.plot(xpoints, ls = '-.')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4, 8, 1, 10])

plt.plot(xpoints, ls = '-.')
plt.plot(xpoints, linewidth = '60')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.plot(y1, ls = ':', lw=2, label='Line 1')
plt.plot(y2, ls = '--', lw=2, label='Line 2')

plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

#--------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')
plt.grid(axis = 'x')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.plot(x,y)


x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.plot(x,y)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 1")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 2")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 3")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 4")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 5")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title("Subplot 6")
plt.plot(x,y)

plt.suptitle("Multiple Subplots Example", fontsize=16, weight='bold')

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.suptitle("Scatter Plot Example", fontsize=16, weight='bold')
plt.xlabel("Water molecules")
plt.ylabel("Calorie Burnage")
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)


x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.suptitle("Comparative Scatter Plot Example", fontsize=16, weight='bold')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()
plt.suptitle("Scatter Plot with Color Mapping", fontsize=16, weight='bold')

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)
plt.colorbar()
plt.suptitle("Scatter Plot with Size Mapping", fontsize=16, weight='bold')
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = np.random.randint(1, 10, size=5)

fig, ax = plt.subplots()

bars = ax.bar(x, y, color='skyblue', edgecolor='black')


for bar in bars:
    bar.set_facecolor('lightblue')
    bar.set_edgecolor('darkblue')
    bar.set_linewidth(1.5)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D


x = np.arange(5)
y = np.random.randint(1, 10, size=5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.bar(x, y, zs=0, zdir='y', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Value')

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
z = np.zeros_like(x)  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

sc = ax.scatter(x, y, z, c=colors, cmap='viridis')

plt.colorbar(sc)
plt.suptitle("Scatter Plot with Color Mapping", fontsize=16, weight='bold')

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.bar(x, y, color = "red")

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.suptitle("Histogram Example", fontsize=16, weight='bold')
plt.hist(x)
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.random.normal(170, 10, 250)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.suptitle("Histogram Example", fontsize=16, weight='bold')
plt.hist(x)
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

y = np.array([35, 25, 25, 15])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(4)
y_pos = np.arange(4)
z = np.zeros(4)
dx = np.ones(4)
dy = np.ones(4)
dz = y

ax.bar3d(x, y_pos, z, dx, dy, dz)
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 
#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

sizes = [25, 30, 20, 15, 10]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(sizes)))  

explode = [0.1, 0.15, 0.05, 0.1, 0.2]

fig, ax = plt.subplots(figsize=(8, 8), facecolor='lightgrey')

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=140,
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
)


plt.setp(autotexts, size=12, weight="bold", color="white",
         path_effects=[path_effects.withStroke(linewidth=2, foreground="black")])
plt.setp(texts, size=12, weight="bold")

plt.suptitle("Fruit Distribution Pie Chart", fontsize=18, fontweight='bold', color='darkblue')

circle = plt.Circle((0,0), 1.05, color='lightblue', alpha=0.2, zorder=0)
ax.add_artist(circle)

plt.show()

#--------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

sizes = [25, 30, 20, 15, 10]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(sizes)))


base_explode = [0.05, 0.07, 0.03, 0.05, 0.08]

fig, ax = plt.subplots(figsize=(8, 8), facecolor='lightgrey')
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    explode=base_explode,
    colors=colors,
    shadow=True,
    startangle=140,
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
)

plt.setp(autotexts, size=12, weight="bold", color="white",
         path_effects=[path_effects.withStroke(linewidth=2, foreground="black")])
plt.setp(texts, size=12, weight="bold")

plt.suptitle("Fruit Distribution Pie Chart", fontsize=18, fontweight='bold', color='darkblue')

circle = plt.Circle((0,0), 1.05, color='lightblue', alpha=0.2, zorder=0)
ax.add_artist(circle)


original_centers = [wedge.center for wedge in wedges]

def on_click(event):
   
    if event.inaxes != ax:
        return
        
    for i, wedge in enumerate(wedges):
        
        if wedge.contains(event)[0]:
            current_center = wedge.center
            orig_center = original_centers[i]
            
            
            if current_center == orig_center:
                theta = (wedge.theta2 + wedge.theta1) / 2
                dx = 0.15 * np.cos(np.deg2rad(theta))
                dy = 0.15 * np.sin(np.deg2rad(theta))
                wedge.set_center((orig_center[0] + dx, orig_center[1] + dy))
            else:
                
                wedge.set_center(orig_center)

            fig.canvas.draw_idle()
            break  

fig.canvas.mpl_connect("button_press_event", on_click)
plt.show()

#--------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()