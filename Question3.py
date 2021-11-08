# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 13:21:05 2021

@author: maxpr
"""
import numpy as np 
import random
import matplotlib.pyplot as plt



"""
This method generates 2 random arrays of size n- X and Z. The X array reperesents
users who clicked on an ad (1 for clicked 0 for no click). The Z array represents
a fake clicks that will be added as noise to create the A array. The A array 
represents the total number of actual clicks until a timestep, with the addition 
of an independent fake click at every timestep.  

"""
def clicks(n):
    x = np.random.randint(2, size = n)
    z = np.random.randint(2, size = n)

    aList = []
    
    for i in range(n):
        previous = x[0:i].sum()
        a = previous + x[i] + z[i]
        aList.append(a)
        
     
    return aList, x

"""
This method reconstructs an array based on the difference between the curent 
element and the previous. If it is:
    -1: previous element had a fake person so we change it to 0 or 1 depending
        on what the previous difference was
        
    0: no fake or real person added, add 0 to reconstructed x array
    
    1: Either a fake or real person was added, add either 0 or 1 randomly to 
       reconstructed x array
    
    2: Both a real and a fake person was added, add a 1 to reconstructed array
"""
def reconstruct_parta(a):
    r = []                                         #reconstructed x array
    for i in range(len(a)):  
        if i>0:
            difference = a[i] - a[i-1]             #difference between current and
                                                   #last element       
            if difference == -1:          
                if i>1:
                    difference = a[i-1]-a[i-2] -1  #recalculate difference without
                                                   #fake person
                    if difference == 0:            
                        r[i-2] = 0
                        r.append(0)
                        
                    else:
                        r[i-2] = 1        
                        r.append(0)
                else:
                    r[i-1] = 0
                    r.append(0)
            elif difference == 0:     
                r.append(0)
            elif difference == 1:      
                r.append(random.randint(0,1))
            else:
                r.append(1)                       
                                          
        else:                                       #edge case at begining of array 
            if a[i] == 0:
                r.append(a[i])
            elif a[i] == 1:
                r.append(random.randint(0,1))
            else:
                r.append(1)
    return r
"""
This method reconstructs an array based on the difference between the curent 
element and the previous element of a give A array. If it is:
    -1: previous element had a fake person so we change it to 0 or 1 depending
        on what the previous difference was
        
    0: no fake or real person added, add 0 to reconstructed x array
    
    1: Either a fake or real person was added, add the element from the given
       W array, which has a 2/3 chance of being correct
    
    2: Both a real and a fake person was added, add a 1 to reconstructed array
"""
def reconstruct_partb(a,w):
    r = []                                         #reconstructed x array
    for i in range(len(a)):  
        if i>0:
            difference = a[i] - a[i-1]             #difference between current and
                                                   #last element       
            if difference == -1:          
                if i>1:
                    difference = a[i-1]-a[i-2] -1  #recalculate difference without
                                                   #fake person
                    if difference == 0:            
                        r[i-2] = 0
                        r.append(0)
                        
                    else:
                        r[i-2] = 1        
                        r.append(0)
                else:
                    r[i-1] = 0
                    r.append(0)
            elif difference == 0:     
                r.append(0)
            elif difference == 1:      
                r.append(w[i])
            else:
                r.append(1)                       
                                          
        else:                                       #edge case at beginning of array 
            if a[i] == 0:
                r.append(a[i])
            elif a[i] == 1:
                r.append(w[i])
            else:
                r.append(1)
    return r

"""
This function creates an array W where each element is a guess that is the same 
as the same element in the X array with a probability of 2/3.
"""
def createGuesses(x):
    w = []
    count0 = 0
    count1 = 0
    for i in range(len(x)):
        prob = np.random.choice([0,1], p=[.33, .67])
        if prob > 0:
            w.append(x[i])

        else:
            count0 += 1
            if x[i] == 0:
                w.append(1)
                
            else:
                w.append(0)
    count = 0
    for i in range(len(x)):
        if w[i] == x[i]:
            count += 1
    return w


def calculate(n):
    aList, xList = clicks(n)
    xGuessA = reconstruct_parta(aList)
    countA = 0
    for i in range(n):
        if xGuessA[i] == xList[i]:
            countA += 1
            
    w = createGuesses(xList)
    xGuessB = reconstruct_partb(aList,w)
    countB = 0
    for i in range(n):
        if xGuessB[i] == xList[i]:
            countB += 1
    
    meanA = countA/n
    meanB = countB/n
    
    return meanA,meanB

"""
Run 20 times when n = 100, 500, 1000, 5000 and calculates mean and std deviation
"""
trials = 20

meanA100List = []
meanA500List = []
meanA1000List = []
meanA5000List = []

meanB100List = []
meanB500List = []
meanB1000List = []
meanB5000List = []

for i in range(20):
    a, b = calculate(100)
    meanA100List.append(a)
    meanB100List.append(b)
    
    meanA100 = np.mean(meanA100List)
    stdevA100 = np.std(meanA100List)
    
    meanB100 = np.mean(meanB100List)
    stdevB100 = np.std(meanB100List)
    
    
    a, b = calculate(500)
    meanA500List.append(a)
    meanB500List.append(b)
    
    meanA500 = np.mean(meanA500List)
    stdevA500 = np.std(meanA500List)
    
    meanB500 = np.mean(meanB500List)
    stdevB500 = np.std(meanB500List)
    
    
    a, b = calculate(1000)
    meanA1000List.append(a)
    meanB1000List.append(b)
    
    meanA1000 = np.mean(meanA1000List)
    stdevA1000 = np.std(meanA1000List)
    
    meanB1000 = np.mean(meanB1000List)
    stdevB1000 = np.std(meanB1000List)
    
    
    a, b = calculate(5000)
    meanA5000List.append(a)
    meanB5000List.append(b)

    meanA5000 = np.mean(meanA5000List)
    stdevA5000 = np.std(meanA5000List)

    meanB5000 = np.mean(meanB5000List)
    stdevB5000 = np.std(meanB5000List)


# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
A = [meanA100, meanA500, meanA1000, meanA5000]
B = [meanB100, meanB500, meanB1000, meanB5000]
 
# Set position of bar on X axis
br1 = np.arange(len(A))
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, A, color ='r', width = barWidth,
        edgecolor ='grey', label ='Part A Mean')
plt.bar(br2, B, color ='b', width = barWidth,
        edgecolor ='grey', label ='Part B Mean')

# Adding Xticks
plt.xlabel('Size', fontweight ='bold', fontsize = 15)
plt.ylabel('Average Mean', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(A))], ['100', '500', '1000', '5000'])
 
plt.legend()
plt.show()
