import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
final_temp = .01   # final temperature
b = 0.9995 # reducing factor of temperature
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
# low_x=-5.12 #limits of dimensions that we move around
# up_x=5.12    #rastrigin
# low_y=-5.12
# up_y=5.12
# low_x=-5      #ackley
# up_x=5
# low_y=-5
# up_y=5
# low_x=-512    #eggholder
# up_x=512
# low_y=-512
# up_y=512
# low_x=-500  #schwefel
# up_x=500
# low_y=-500
# up_y=500
low_x=-10  #easom#shubert#alpine
up_x=10
low_y=-10
up_y=10
# low_x=-2  #sphere
# up_x=2
# low_y=-2
# up_y=2
num_of_iter=1000 #number of experiment iterations

for exp in range(0, num_of_iter):
    start_time=time.process_time()
    T = 100 # starting temperature
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
    
#     z=rastrigin(x, y, A)
#     z=ackley(x, y)
#     z=eggholder(x, y)
#     z = schwefel(x, y)
#     z = easom(x, y)
#     z = sphere(x, y)
    z = shubert(x, y)
    
    while T>final_temp:
        if x-neighbor_distance>low_x: #setting lower limits
            lower = x - neighbor_distance
        else:
            lower = low_x
            
        if x+neighbor_distance<up_x: #setting upper limits
            upper = x + neighbor_distance
        else:
            upper=up_x
        neighbor_x = random.uniform(lower, upper)
        
        if y-neighbor_distance>low_y: #setting lower limits
            lower = y - neighbor_distance
        else:
            lower = low_y
          
        if y+neighbor_distance<up_y: #setting upper limits
            upper = y + neighbor_distance
        else:
            upper = up_y
        neighbor_y = random.uniform(lower, upper)
    
#         DE = z - rastrigin(neighbor_x, neighbor_y, A) #cost difference
#         DE = ackley(x, y) - ackley(neighbor_x, neighbor_y)
#         DE = eggholder(x, y) - eggholder(neighbor_x, neighbor_y)
#         DE = schwefel(x, y) - schwefel(neighbor_x, neighbor_y)
#         DE = easom(x, y) - easom(neighbor_x, neighbor_y)
#         DE = sphere(x, y) - sphere(neighbor_x, neighbor_y)
        DE = shubert(x, y) - shubert(neighbor_x, neighbor_y)

        if DE > 0:   # if the neighbor is better, accept it
            x = neighbor_x
            y = neighbor_y
        else:   # if not, accept it with a probability
            if random.uniform(0, 1) < math.exp(DE / T):
                x = neighbor_x
                y = neighbor_y
        
#         z = rastrigin(x, y, A)
#         z = ackley(x, y)
#         z = eggholder(x, y)
#         z = schwefel(x, y)
#         z = easom(x, y)
#         z = sphere(x, y)
        z = shubert(x, y)
        
        T=b*T
        #print("Iteration ",i,": x =",x," y =",y," z =",z)
    print(exp)
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Simulated Annealing it is found that it takes ",time_average," seconds and to have an accuracy of ",results_average, " from the global minimum")

import xlwt 
from xlwt import Workbook 
        
wb = Workbook() 
         
sheet1 = wb.add_sheet('SA_shubert')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
            
wb.save('SA_shubert.xls')
print("All saved")