import numpy as np
import matplotlib.pyplot as plt
import csv

# f = open('ans.csv', 'r')

x_axis = [i for i in range(10, 100, 5)]
a = []
b = []
c = []
d = []
e = []
f = []
g = []

with open('funny1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == '100':
            a.append((float(row[2]) - 0.1)/1000000)
        elif row[0] == '140':
            b.append((float(row[2]) - 0.1)/1000000)
        elif row[0] == '160':
            c.append((float(row[2]) - 0.1)/1000000)
        elif row[0] == '180':
            d.append((float(row[2]) - 0.1)/1000000)
        elif row[0] == '320':
            e.append((float(row[2]) - 0.1)/1000000)
        elif row[0] == '384':
            f.append((float(row[2]) - 0.1)/1000000)
        else:
            g.append((float(row[2]) - 0.1)/1000000)

print('completed reading {} {} {}'.format(len(a), len(b), len(c)))



# plt.plot(x_axis, a, 'r--', x_axis, b, 'b--', x_axis, c, 'g--', x_axis, d, 'c--')
# plt.plot(x_axis, a, x_axis, b, 'b--', x_axis, b, 'g--', x_axis, d, 'r--', x_axis, e, 'k--', x_axis, f, 'y--', x_axis, g, 'c--')

plt.show()
