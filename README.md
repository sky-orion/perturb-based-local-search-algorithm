# perturb-based-local-search-algorithm
Reproduction of the paper "An Effective Local Search Algorithm for the Multidepot Cumulative Capacitated Vehicle Routing Problem"  
Used to solve mdccvrp problems,dataset from this website http://www.bernabe.dorronsoro.es/vrp/ 
there are six local search operators and two perturbation operators in the original paper are reproduced.  
there have two version of PLS, PLS2 is close to the original expression, PLS1 replaces s with gbest in each iteration, and the performance of PLS1 is slightly better than that of PLS2，the performance gap is about 20% compared to the original paper.  
## To use
```
python PLS2.py
```



