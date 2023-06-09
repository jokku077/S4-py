import matplotlib.pyplot as plt

heights = ['135-140', '140-145', '145-150', '150-155']
students = [4, 12, 16, 8]
c=['Height']
plt.hist(heights, bins=len(heights), weights=students,color='green')
plt.title('Height of Students')
plt.xlabel('Height (in cm)')
plt.ylabel('Number of Students')
plt.legend(c)
plt.show()
