import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels = ["school expense ","college expense","home expense","extra expense"]
myexplode = [0.2,0,0,0]
plt.pie(y, labels = mylabels , explode = myexplode , shadow = True)
plt.show()