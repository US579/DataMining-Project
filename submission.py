# -*- codeing:utf-8 -*-
import numpy as np
import pandas as pd
from collections import defaultdict

# Question 1
def viterbi_algorithm(State_File, Symbol_File, Query_File): # do not change the heading of the function
    states = []
    observations = []
    with open(State_File) as f1:
        n1 = int(f1.readline())
        distance = [[0 for _ in range(n1)] for _ in range(n1)]
        transition_probability = [[0 for _ in range(n1)] for _ in range(n1)]
        for i in range(n1):
            states.append(f1.readline().strip())
        st = f1.readlines()
        lis = [j.strip().split() for j in st]
        for i in lis:
            distance[int(i[0])][int(i[1])] = int(i[2])
        for i in range(n1):
            for j in range(n1):
                if j == states.index("END") or i == states.index("BEGIN"):
                    print('{} {}'.format(i,j))
                    continue
                transition_probability[i][j] = (float(distance[i][j])+1) / (sum(distance[i])+n1-1)


    with open(Symbol_File) as f2:
        n2 = int(f2.readline())
        emission_probability = [[0 for _ in range(n2)] for _ in range(n2)]
        distance2 = [[0 for _ in range(n2)] for _ in range(n2)]
        for i in range(n2):
            observations.append(f2.readline().strip())
        st2 = f2.readlines()
        lis2 = [j.strip().split() for j in st2]
    for i in lis2:
        distance2[int(i[0])][int(i[1])] = int(i[2])
    for i in range(n2):
        for j in range(n2):
            emission_probability[i][j] = (float(distance2[i][j])+1) / (sum(distance2[i]) + n2 +1)

    pi = {0:1/5,1:1/5,2:1/5,3:1/5,4:1/5}
    obs = []
    #print(states)
    #print(observations)
    #print(transition_probability)
    #print(emission_probability)

    #transition_probability = np.array(transition_probability)
    #emission_probability = np.array(emission_probability)
    #pi = np.array(pi)
    print(transition_probability)
    print(emission_probability)
    v = [{}]
    path = dict()
    print(states)
    print(n1)
    for y in range(n2):
        v[0][y] = pi[y] * emission_probability[y][0]
        path[y] = [y]
    print(v)
    print(path)










State_File ='./toy_example/State_File'
Symbol_File='./toy_example/Symbol_File'
Query_File ='./toy_example/Query_File'
viterbi_result =viterbi_algorithm(State_File, Symbol_File, Query_File)


# Question 2
def top_k_viterbi(State_File, Symbol_File, Query_File, k): # do not change the heading of the function
    pass # Replace this line with your implementation...


# Question 3 + Bonus
def advanced_decoding(State_File, Symbol_File, Query_File): # do not change the heading of the function
    pass # Replace this line with your implementation...
