f = open('sample.txt','r')
line = f.read().split()
x = int(line[0])
y = int(line[1])
z = int(line[2])


for i in range(1,z):
    if i % x == 0:
        print 'F',
    elif i % y == 0:
        print 'B',
    else:
        print 'FB',
