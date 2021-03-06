import matplotlib.pyplot as plt


x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubed Values", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig("five_thousand_cube_cmap.png", bbox_inches='tight')
plt.show()
