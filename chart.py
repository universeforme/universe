import matplotlib.pyplot as plt

# x = [1, 3, 5, 7, 10]
# y = [6, 2, 1, 1.5, 9] 
# x2 = [2, 4, 4, 8, 9] 
# y2 = [3, 3, 6, 1, 6]


# plt.bar(x,y,label="line 1",color="salmon")
# plt.bar(x2,y2,label="line 2",color="black")
# plt.title('datascience')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend()

# plt.show()

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [5, 7, 3, 4, 4, 6, 1, 7, 9]
# plt.scatter(x, y, label="Creative Institute", color="maroon",marker="x") 
# plt.xlabel("X-Axis Name")
# plt.xlabel("Y-Axis Name")
# plt.title("Scatter Plots / Scatter Graph") 
# plt.legend()
# plt.show()

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 7.5, 9, 12] 
working = [3, 6, 5, 4, 2] 
exercise = [1, 0.5, 1, 0.5, 0.5] 
study = [2, 3, 2, 4, 6]
plt.stackplot(days,sleeping,working,exercise,study,labels=['days','sleeping','wor king','exercise','study'])
plt.legend()
plt.show()