import matplotlib.pyplot as plt
import numpy as np

plt.rc("text", usetex=True)
plt.rcParams["mathtext.fontset"] = "cm"

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)

a, b = 2, 2
theta = np.arange(0, 2 * np.pi, np.pi / 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)
ax.plot(x, y - 1, "r", lw=".75")
ax.plot(x, y + 1, "b", lw=".75")

ax.set_ylim([-4, 4])
ax.set_xlim([-4, 4])

ax.fill_between(
    x,
    1 - np.sqrt(4 - pow(x, 2)),
    np.sqrt(4 - pow(x, 2)) - 1,
    where=(x >= -np.sqrt(3)) & (x <= np.sqrt(3)),
    color="y",
)

plt.xlabel(r"$a$")
plt.ylabel(r"$b$")

plt.savefig("ellipse_area.pdf")
plt.show()
