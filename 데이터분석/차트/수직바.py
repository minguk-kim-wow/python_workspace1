import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(1234)
plt.rcdefaults()
fig, ax = plt.subplots()

# 수평바 
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people)) #사람 숫자만큼 0~ 4 까지 y값 생성 

#각자 
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.bar(y_pos, performance, yerr=error, align='center')


ax.set_xticks(y_pos) #축 눈금 
ax.set_xticklabels(people) # y축 라벨 

ax.set_ylabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()