from collections import Counter
import matplotlib.pyplot as plt    

woord = "matplotlib"
frequentie = Counter(woord)
print(frequentie)

plt.bar(list(frequentie.keys()),list(frequentie.values()))
plt.show()