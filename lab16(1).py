import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(-4,4,51)
y = np.sin(np.pi + x) +0.1*np.cos(x)    
plt.plot(x,y,'c-', label ='sin(п+x) + 0.1*cos(x)', marker = 's')    
plt.axis([-4, 4, -2.5,2.5]) 
plt.xlabel('x') 
plt.ylabel('y')
plt.legend()
plt.show()
plt.savefig("picture.png", dpi=400)