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



with open('100.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a.append((float(row[2]) - 0.1)/1000000)


with open('140.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        b.append((float(row[2]) - 0.1)/1000000)
           

with open('160.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        c.append((float(row[2]) - 0.1)/1000000)


with open('180.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        d.append((float(row[2]) - 0.1)/1000000)
           

with open('320.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        e.append((float(row[2]) - 0.1)/1000000)


with open('384.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f.append((float(row[2]) - 0.1)/1000000)
           

with open('512.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        g.append((float(row[2]) - 0.1)/1000000)


# print('completed reading {} {} {}'.format(len(a), len(b), len(c)))


# l1 = plt.plot(x_axis, a, 'r--', label='100')
# l2 = plt.plot(x_axis, b, 'r--', label='140')
# plt.legend(handles=[l1, l2])
# plt.show()


# plt.plot(x_axis, a, 'r--', label='100', x_axis, b, 'b--', label='140', x_axis, c, 'g--', label='160', x_axis, d, 'c--',label='180')
# plt.xlabel('Length of Random String')
# plt.ylabel('Execution Time (in Microseconds)')
# plt.show()


plt.plot(x_axis, e, 'r--', x_axis, f, 'b--', x_axis, g, 'g--')
# plt.xlabel('Length of Random String')
# plt.ylabel('Execution Time (in Microseconds)')
plt.show()
