import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('HelloWorld_Plot', fontsize=14, fontweight='bold')

fig.subplots_adjust(top=0.85)

ax = fig.add_subplot(111)
ax.set_xlabel('Hello')
ax.set_ylabel('World')

ax.text(4, 5, 'Hello "World', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
ax.axis([0, 10, 0, 10])

plt.show()
