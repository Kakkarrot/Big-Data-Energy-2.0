# import matplotlib.pyplot as plt

histogram_file = "../Case1_Data/case1-concurrent-sessions-histogram.txt"

file = open (histogram_file, 'r')
lines = file.readlines()

for line in lines:
    print(line)