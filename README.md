# Jaya-Optimizer

Jaya optimization algorithm is a heuristic algorithm that does not require any control parameters besides the common parameters like number of generations and population size, introduced in paper "Jaya: A simple and new optimization algorithm for solving constrained and unconstrained optimization problems" . This makes jaya algorithm easier to use than other heuristic algorithms like Genetic algorithm and PSO. I have implemented it in Python. 

Modified - Jaya

Expolaration - It means searching a large portion of the search space in order to find a better solution. It is also called diversification.
Exploitation - It means searching in the region identified to have better solution than others. It is also called intensification.

Expolaration and exploitation are at conflict with each other. If more time is spend on one, the other is neglected. In this modification an approach to simultaneous exploration and exploitation to modify the population has been proposed. 

When a promising solution is found, three scenarios are possible - 
1.	It is the best Solution.
2.	It is the local optimum and the global optimum is far away.
3.	The global optimum is near this solution.

In the first case the algorithm has achieved its purpose and no further optimization can be done in future iterations. In the second case the technique of exploration should be used and in the third case exploitation should be used.

Modified Jaya has done better than Jaya on 5 of the 6 benchmark functions.
