import matplotlib.pyplot as plt

from die import Die


die_1 = Die()
die_2 = Die()
die_3 = Die()

results = (
    [die_1.roll()+die_2.roll()+die_3.roll() for n in range(50000)]
    )
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequency = [results.count(value) for value in range(3, max_results+1)]

possible_rolls = range(3, max_results+1)

fig, ax = plt.subplots()
ax.bar(possible_rolls, frequency, tick_label=possible_rolls)
ax.set_title("Results of rolling three D6 50,000 times")
ax.set_xlabel("Possible Rolls")
ax.set_ylabel("Frequency")

plt.savefig('die_visual_matplotlib.png', bbox_inches='tight')
plt.show()
