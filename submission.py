# -*- codeing:utf-8 -*-
import numpy as np
import pandas as pd
from collections import defaultdict
import math
# Question 1
def viterbi_algorithm(State_File, Symbol_File, Query_File): # do not change the heading of the function
    states = []
    sym = []
    with open(State_File) as f1:
        n1 = int(f1.readline())
        Pi = {k: 0 for k in range(n1)}
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
                end, begin =  states.index("END"),states.index("BEGIN")
                if i == end or i == begin or j == end or j == begin :
                    if i ==  begin:
                        Pi[j] = (float(distance[i][j])) / (sum(distance[i]))
                    continue
                transition_probability[i][j] = (float(distance[i][j])+1) / (sum(distance[i])+n1-1)

    with open(Symbol_File) as f2:
        n2 = int(f2.readline())
        emission_probability = [[0 for _ in range(n2)] for _ in range(n2)]
        distance2 = [[0 for _ in range(n2)] for _ in range(n2)]
        for i in range(n2):
            sym.append(f2.readline().strip())
        st2 = f2.readlines()
        lis2 = [j.strip().split() for j in st2]
    for i in lis2:
        distance2[int(i[0])][int(i[1])] = int(i[2])
    for i in range(n2):
        for j in range(n2):
            emission_probability[i][j] = (float(distance2[i][j])+1) / (sum(distance2[i]) + n2 +1)

    with open(Query_File) as f3:
        n3 = f3.readlines()
        obs = [x.strip().split() for x in n3]
        obs = obs[1]

    print('obs',obs)
    print('states',states)
    print('sym',sym)
    print('transition_probability',transition_probability)
    print('emission_probability',emission_probability)
    print('Pi',Pi)

    path = {s:[] for s in states}

    curr_pro = {}
    for s in states[:len(states)-2]:
        curr_pro[s] = Pi[states.index(s)]*emission_probability[states.index(s)][sym.index(obs[0])]
    print(curr_pro)
    for i in range(1,len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for cur in range(len(states[:len(states)-2])):

            try:
                max_pr,last_pr = max(((last_pro[k] * transition_probability[states.index(k)][cur]*
                                       emission_probability[cur][sym.index(obs[i])], k) for k in states[:3]))
            except:
                max_pr, last_pr = max(((last_pro[k] * transition_probability[states.index(k)][cur] *
                                        ( 1 / obs.count(obs[i]) + n2 + 1 ) , k) for k in states[:3]))
            curr_pro[states[cur]] = max_pr
            path[states[cur]].append(last_pr)

    max_pr=max(curr_pro,key=lambda x:curr_pro[x])
    print(math.log(curr_pro[max_pr]))
    lis_z = [3,states.index(max_pr)]
    for i in path[max_pr]:
        lis_z.append(states.index(i))
    lis_z.extend([4,math.log(curr_pro[max_pr])])
    print(lis_z)















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
