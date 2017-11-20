import numpy as np
import matplotlib.pyplot as plt

N = 4
menMeans = (0.785,0.76,0.875,0.89)
womenMeans = (0.,0.,0.09,0.11)
lose = (0.39,0.34,0.45,0.5)
ind = np.arange(N)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, color='blue')
p2 = plt.bar(ind + width, womenMeans, width, color='yellow')
p3 = plt.bar(ind + 2*width, lose, width, color='red')

plt.ylabel('Accuracy')
#plt.title('Scores by group and gender')
plt.xticks(ind+width/2.,('SVM-linear', 'LogisticR', 'SVM-RBF', 'SVM-RBF-ONLINE'))
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0],p2[0],p3[0]),('win','draw','lose'))

plt.show()