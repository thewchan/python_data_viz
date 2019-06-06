import matplotlib.pyplot as plt

from random_walk import RandomWalk


grain_path = RandomWalk(5000)
grain_path.fill_walk()
point_numbers = range(grain_path.num_points)

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.plot(
    grain_path.x_values, grain_path.y_values, linewidth=1,
    c='blue'
    )
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('pollen_grain.png', bbox_inches='tight')
plt.show()
