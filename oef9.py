import numpy  as np 
import matplotlib.pyplot as plt    

activiteiten = ["Studeren", "Sport", "Slapen", "Vrije tijd"]

uren = np.array([5, 2, 8, 9])
plt.pie(uren,labels=activiteiten)
plt.show()