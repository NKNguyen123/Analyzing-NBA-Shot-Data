from pprint import pprint
import math
import matplotlib.pyplot as plt

def distance(x,y):
    return int(math.floor(math.sqrt(x**2 + y**2)))

files=['Steph_Curry.txt','Chris_Paul.txt', 'Zion_Williamson.txt']
data=[]
for file in files:
    temp_file=open(file, 'r')
    content=temp_file.read()
    content_list=content.split('\n')
    content_list.pop(-1)
    temp_data=[]
    for c in content_list:
        temp=eval(c)
        temp[0]=temp[0]/12
        temp[1]=temp[1]/12
        temp_data.append(temp)
    data.append(temp_data)

ranges=[[0,100],[0,10],[10,22],[22,100]]
spots=[]
for d in data:
    temp_spots=[]
    for r in ranges:
        x_hits=[]
        y_hits=[]
        x_misses=[]
        y_misses=[]
        for shot in d:
            if r[0]<=distance(shot[0],shot[1])<r[1]:
                if shot[2]:
                    x_hits.append(shot[0])
                    y_hits.append(shot[1])
                else:
                    x_misses.append(shot[0])
                    y_misses.append(shot[1])
        temp_spots.append([x_hits,y_hits,x_misses,y_misses])
    spots.append(temp_spots)

fig, axs = plt.subplots(3,4)

titles=[
['Steph Curry All', 'Steph Curry Close Range', 'Steph Curry Mid Range', 'Steph Curry Long Range'],
['Chris Paul All', 'Chris Paul Close Range', 'Chris Paul Mid Range', 'Chris Paul Long Range'],
['Zion Williamson All', 'Zion Williamson Close Range', 'Zion Williamson Mid Range', 'Zion Williamson Long Range']
]

galpha=0.7
ralpha=0.3
gmark='.'
rmark='.'
xlim=[-25,25]
ylim=[0,50]

for player in range(3):
    for range_ in range(4):
        axs[player,range_].scatter(spots[player][range_][0], spots[player][range_][1], marker=gmark, color='green', alpha=galpha)
        axs[player,range_].scatter(spots[player][range_][2], spots[player][range_][3], marker=rmark, color='red', alpha=ralpha)
        axs[player,range_].set_xlim(xlim)
        axs[player,range_].set_ylim(ylim)
        axs[player,range_].set_title(titles[player][range_])

fig.suptitle("Shot Data")
for ax in axs.flat:
    ax.set(xlabel='Width of Court (ft.)', ylabel='Length of Court (ft.)')
for ax in axs.flat:
    ax.label_outer()
plt.show()
