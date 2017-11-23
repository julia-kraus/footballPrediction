import numpy as np
import matplotlib.pyplot as plt

N = 1
wincorrect = (0.9)
drawcorrect = (0.)
losscorrect = (0.3)
ind = np.arange(N)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, wincorrect, width, color='blue')
p2 = plt.bar(ind + width, drawcorrect, width, color='yellow')
p3 = plt.bar(ind + 2*width, losscorrect, width, color='red')

plt.ylabel('Accuracy')
plt.title('Accuracy for win draw and loss')
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0],p2[0],p3[0]),('win','draw','loss'))

plt.show()