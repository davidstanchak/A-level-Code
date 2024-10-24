# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# height length = n,
# 2 <= n <= 105
# 0 <= height[i] <= 104
# find maximum amount of water a container can hold. try to get widest but highest aswell. 2 bars are to be used as walls.
import random
import numpy

n = random.randint(2, 10**5)
height = random.choices(range(0, 10**4), k=n)
height = numpy.sort(height)
print(height[100])