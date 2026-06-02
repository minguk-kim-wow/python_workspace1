import matplotlib.pyplot as plt
import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#화면크기 
plt.figure(figsize=(9, 3))

#차트 영역을 1,2,3 세개로 나누고 1번 영역에 그림을 그린다 
plt.subplot(131)
plt.bar(names, values)#막대그래프

plt.subplot(132)
plt.scatter(names, values) #산포도

plt.subplot(133)
plt.plot(names, values) #꺽은선

plt.suptitle('Categorical Plotting')
plt.show()