# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# height length = n,
# 2 <= n <= 105
# 0 <= height[i] <= 104
# find maximum amount of water a container can hold. try to get widest but highest aswell. 2 bars are to be used as walls.
import random
import numpy

#n = random.randint(2, 10**5)
n = 20
bars = random.choices(range(0, 10**4), k=n)
'''
midpoint = n//2 #truncated 
half_areas = [None] * n #creating array with contents 'None' and length 'n' for memory efficiency
for i in range(n):
    half_areas[i] = bars[i]*(midpoint-i)
        
print(half_areas)
'''
'''
eighth = n//8
sectionIndex, n_Increment = 0, 0
sectioned_Bars = ['e'] * n
section_Length = len(sectioned_Bars[sectionIndex])

while (sectionIndex < 8) and (n_Increment != section_Length):

    section_Length = len(sectioned_Bars[sectionIndex])

    sectioned_Bars = numpy.reshape(sectioned_Bars,(sectionIndex,section_Length))
    

    for i in range(eighth):
        if i != eighth:
            sectioned_Bars[sectionIndex,i] = bars[n_Increment]
            n_Increment +=1
        else:
            sectionIndex+=1

    sectioned_Bars = numpy.reshape(sectioned_Bars,(sectionIndex,n_Increment))

    for i in reversed(range(section_Length)):
        if i != -1:
            sectioned_Bars[(7-sectionIndex),i] = bars[n-(section_Length*sectionIndex)]
            n_Increment +=1
        else:
            sectionIndex+=1
    print(sectioned_Bars)'''

    #sort_sectioned_Bars = sectioned_Bars[sectionIndex].sort(reverse=True)

    
    

'''

    n_increment+=1
print(sectioned_Bars)


for i in range(eighth):

right_first_quarter_array = bars[eighth]
left_first_quarter_array.sort(reverse=True)
for i in range(eighth):
'''






    