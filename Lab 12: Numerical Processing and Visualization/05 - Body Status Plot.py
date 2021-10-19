import numpy as np
import matplotlib.pyplot as plt
inp = np.loadtxt(input('Enter file name: '), delimiter=',')
bmi = inp.T[0] / (inp.T[1]/100)**2
plt.scatter(inp.T[0], inp.T[1], c=bmi)
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.grid(True)
bar = plt.colorbar()  # add a color bar
bar.ax.set_title("BMI")  # add title to the color bar
plt.set_cmap("jet")  # set color mapping scheme to "jet"
plt.show()