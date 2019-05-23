import numpy as np
from random import random, randint, uniform
import copy
import sys
from math import cos, exp, sqrt

def fitness( x, dimensions, f ):
    
    if f == 1:
        ans = -20 * exp( -0.2 * sqrt( 0.5*(x[0]**2 + x[1]**2) ) ) - exp( 0.5*( cos(2*3.14*x[0]) + cos(2*3.14*x[1]) ) ) + exp(1) + 20
        return ans
    if f == 2:
        ans = ( 1.5 - x[0] + x[0]*x[1] )**2 + ( 2.25 - x[0] + x[0]*(x[1]**2) )**2 + (2.625 - x[0] + x[0]*(x[1]**3))**2
        return ans
    if f == 3:
        ans = ( x[0] + 2*x[1] - 7)**2 + ( 2*x[0] + x[1] - 5)**2
        return ans
    if f == 4:
        ans = -cos(x[0])*cos(x[1])*exp( -((x[0]-3.14)**2 + (x[1]-3.14)**2))
        return ans
    if f==5:
        ans = 0.26*( x[0]**2 + x[1]**2 ) - 0.48*x[0]*x[1]
        return ans
    if f == 6:
        s = 0
        for i in range(dimensions):
            s = s + x[i]**2 - 10*cos(2*3.14*x[i])
        return 10*dimensions + s
    if f==7:
        s = 0
        for i in range(dimensions-1):
            s = s + 100 * ( x[i+1] - x[i]**2 ) ** 2 + ( 1 - x[i] )**2
        return s
    else:
        return 0
    

def jaya_opt(f):
    
    gens = 100
    pop_size = 40
    

    if f == 1:
        dimensions = 2
        min_value = -5
        max_value = 5
    if f == 2:
        dimensions = 2
        min_value = -4.5
        max_value = 4.5
    if f == 3:
        dimensions = 2
        min_value = -10
        max_value = 10
    if f == 4:
        dimensions = 2
        min_value = -100
        max_value = 100
    if f == 5:
        dimensions = 2
        min_value = -10
        max_value = 10
    if f == 6:
        dimensions = 2
        min_value = -5.12
        max_value = 5.12
    if f == 7:
        dimensions = 10
        min_value = -( pow( 2, 63) - 1 )
        max_value = pow( 2, 63 ) -1

    
    population = np.zeros(( pop_size, dimensions ))
    for i in range(pop_size):
        for j in range(dimensions):
            population[i][j] = uniform( min_value, max_value )   #initializing the population

    best_fitness = sys.maxsize
    best_index = -1
    best_ind = np.zeros(( dimensions ))
    worst_fitness = 0
    worst_index = -1
    worst_ind = np.zeros(( dimensions ))
    fit_matrix = np.zeros(( pop_size ))
    
    
    for i in range( pop_size ):
        fitness_value = fitness( population[i], dimensions, f )  #calculating fitness of every individual
        fit_matrix[i] = fitness_value
        if fitness_value < best_fitness:   #finding best fit element
            best_fitness = fitness_value
            best_index = i
            best_ind = population[i]
        if fitness_value > worst_fitness:   #finding worst fit element
            worst_fitness = fitness_value
            worst_index = i
            worst_ind = population[i]

    for g in range( gens):       # iterating over generations
        #if g == 0 or g==gens-1:
        #print( best_fitness)
        #print(population)
        #print()
        for i in range(pop_size):
            new_value = np.zeros(( dimensions ))
            for j in range(dimensions):
                new_value[j] = population[i][j] + random()*( best_ind[j] - abs(population[i][j]) ) - random()*( worst_ind[j] - abs(population[i][j]))  # jaya equaion
            new_value_fit = fitness( new_value, dimensions, f )
            current_fit = fit_matrix[i]
            if new_value_fit < current_fit:   #replacing current element with new element if it has better fitness
                population[i] = new_value
                fit_matrix[i] = new_value_fit

        
        for i in range( pop_size ):              # finding the best and worst element
            if fit_matrix[i] < best_fitness :
                best_fitness = fit_matrix[i]
                best_fitness_index = i
                best_ind = population[i]

            if fit_matrix[i] > worst_fitness :
                worst_fitness = fit_matrix[i]
                worst_fitness_index = i
                best_ind = population[i]

    #print(best_fitness)
    return best_fitness
        

l = [ 1, 2, 3, 4, 5, 6, 7]

for i in l:     # calculating jaya over 7 benchmark functions, taking the average of 20 runs
    #print(f)
    n = 20
    ans = 0
    for j in range(n):
        ans += jaya_opt(i)
    ans = ans/n

    if i == 1:
        print( 'ackley    ', ans)
    if i == 2:
        print( 'bealey    ', ans)
    if i==3:
        print( 'booth     ',ans)
    if i==4:
        print( 'easom     ', ans)
    if i==5:
        print( 'matyas    ', ans)
    if i==6:
        print( 'rastring   ', ans)
    if i==7:
        print( 'rosenbrock  ', ans)































    

    

    
