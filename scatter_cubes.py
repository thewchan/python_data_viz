import matplotlib.pyplot as plt


x_values = range(1, 5)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=50)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubed Values", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig("five_cube.png", bbox_inches='tight')
plt.show()
