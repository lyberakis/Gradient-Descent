import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
init_T = 100             # initial threshold
rounds = 500000           # number of parts that the threshold sequence will contain
neighbor_distance = 1   # the distance that a possible neighbor can have in x or y dimension
T = np.linspace(init_T, 0, rounds)  #all threshold values for the TA
dimensions= 2

low=-5.12 #limits of dimensions that we move around
up=5.12    #rastrigin
# low_x=-5 #ackley
# up_x=5
# low_y=-5
# up_y=5
# low_x=-512
# up_x=512    #eggholder
# low_y=-512
# up_y=512
# low_x=-500  #schwefel
# up_x=500
# low_y=-500
# up_y=500
# low_x=-10  #easom#shubert#alpine
# up_x=10
# low_y=-10
# up_y=10
# low_x=-2  #sphere
# up_x=2
# low_y=-2
# up_y=2
num_of_iter=1000 #number of experiment iterations

for exp in range(0, num_of_iter):
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))
    z=rastrigin_d(xvals)
#     z=ackley(x, y)
#     z=eggholder(x, y)
#     z=schwefel(x,y)
#     z = easom(x, y)
#     z = sphere(x, y)
#     z = shubert(x, y)
    
    start_time=time.process_time()
    
    for t in T:
        neighbors=[]
        for i in xvals:
            if i - neighbor_distance > low: #setting lower limits
                lower = i - neighbor_distance
            else:
                lower = low
            
            if i + neighbor_distance < up: #setting upper limits
                upper = i + neighbor_distance
            else:
                upper = up
        neighbors.append(random.uniform(lower, upper))
            
        DE = z - rastrigin_d(neighbors) #cost difference
#         DE = ackley(x, y) - ackley(neighbor_x, neighbor_y)
#         DE = eggholder(x, y) - eggholder(neighbor_x, neighbor_y)
#         DE = schwefel(x, y) - schwefel(neighbor_x, neighbor_y)
#         DE = easom(x, y) - easom(neighbor_x, neighbor_y)
#         DE = sphere(x, y) - sphere(neighbor_x, neighbor_y)
#         DE = shubert(x, y) - shubert(neighbor_x, neighbor_y)
        
        if DE > -t:    # if the new solution is better, accept it
            for i in range(0, dimensions):
                xvals[i] = neighbors[i]
            
        z = rastrigin_d(xvals)
#         z=ackley(x, y)
#         z=eggholder(x, y)
#         z=schwefel(x,y)
#         z = easom(x, y)
#         z = sphere(x, y)
#         z = shubert(x, y)
    print(exp)
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
 
import xlwt 
from xlwt import Workbook 
    
wb = Workbook() 
     
sheet1 = wb.add_sheet('TA_shubert')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
        
wb.save('TA_shubert.xls')
print("All saved")