from collections import Counter
import matplotlib.pyplot as plt    

woord = "matplotlib"
frequentie = Counter(woord)
print(frequentie)

plt.bar(str(frequentie),int(frequentie))
plt.show()