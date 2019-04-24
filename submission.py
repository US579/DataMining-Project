# -*- codeing:utf-8 -*-
import math
import numpy as np
# Question 1
def viterbi_algorithm(State_File, Symbol_File, Query_File): # do not change the heading of the function
    states = []
    sym = []
    with open(State_File) as f1:
        n1 = int(f1.readline())
        distance = np.zeros((n1,n1))
        transition_probability = np.zeros((n1,n1))
        for i in range(n1):
            states.append(f1.readline().strip())
        st = f1.readlines()
        lis = [j.strip().split() for j in st]
        for i in lis:
            distance[int(i[0])][int(i[1])] = int(i[2])

        for i in range(n1):
            for j in range(n1):
                transition_probability[i][j] = (float(distance[i][j])+1) / (sum(distance[i])+n1-1)
    with open(Symbol_File) as f2:
        n2 = int(f2.readline())
        emission_probability = {}
        distance2 = {}
        for i in range(n2):
            sym.append(f2.readline().strip())
        st2 = f2.readlines()
        lis2 = [j.strip().split() for j in st2]
    for i in lis2:
        distance2[i[0]+'-'+i[1]] = int(i[2])
    dic_distance = {}
    for i in lis2:
        if int(i[0]) not in dic_distance:
            dic_distance[int(i[0])] = int(i[2])
        else:
            dic_distance[int(i[0])] += int(i[2])

    for i in lis2:
        emission_probability[i[0]+'-'+i[1]] =(float(i[2])+1) / (dic_distance[int(i[0])] + n2 +1)
    with open(Query_File) as f3:
        n3 = f3.readlines()
        obs = [x.strip().split() for x in n3]
    obs = split(obs)
    lis = []
    for obs in obs:
        lis.append(viterbi(states,obs,transition_probability,emission_probability,sym,n2,dic_distance))
    return lis

def split(obs):
    flag = [',','(',')','/']
    lis_sym = []
    lis_s = []
    for k in obs:
        for v in k:
            if v in flag:
                lis_sym.append(v)
                continue
            if v[0] in flag:
                lis_sym.extend([v[0],v[1:]])
                continue
            elif v[-1] in flag:
                lis_sym.extend([v[:-1], v[-1]])
                continue
            lis_sym.append(v)
        lis_s.append(lis_sym)
        lis_sym = []
    return lis_s

def viterbi(states,obs,transition_probability,emission_probability,sym,n2,dic_distance):
    path = {s:[] for s in states}
    curr_pro = {}
    for s in states[:-2]:
        try:
            curr_pro[s] = math.log(transition_probability[len(states)-2][states.index(s)])+\
                          math.log(emission_probability[str(states.index(s))+'-'+str(sym.index(obs[0]))])
        except:
            curr_pro[s] = math.log(transition_probability[len(states)-2][states.index(s)])+\
                          math.log((1/(dic_distance[states.index(s)]+n2 +1)))
    for i in range(1,len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for cur in range(len(states[:-2])):
            try:
                if str(cur)+'-'+str(sym.index(obs[i])) not in emission_probability:
                    emission_rate = 1.0 / (dic_distance[cur] + n2 +1)
                else:
                    emission_rate = emission_probability[str(cur)+'-'+str(sym.index(obs[i]))]
                (max_pr,last_state) = max([(last_pro[k]+math.log(transition_probability[states.index(k)][cur])+
                                            math.log(emission_rate), k) for k in states[:-2]])
            except:
                (max_pr,last_state) = max([(last_pro[k] +math.log(transition_probability[states.index(k)][cur])+
                                            math.log (1.0/(dic_distance[cur]+n2 +1)), k) for k in states[:-2]])
            curr_pro[states[cur]] = max_pr
            path[states[cur]].append(last_state)
    for i in states[:-2]:
        curr_pro[i] = curr_pro[i] + math.log(transition_probability[states.index(i)][len(states)-1])
    max_pr=max(curr_pro,key=lambda x:curr_pro[x])
    lis = [states[-1],max_pr]
    for num in range(len(path[max_pr])-1,-1,-1):
        lis.append(path[lis[-1]][num])
    lis.append(states[-2])
    lis = [states.index(ele) for ele in lis[::-1]]
    lis.append(curr_pro[max_pr])
    # print('obs',obs)
    # print('states',states)
    # print('sym',sym)
    # print('transition_probability',transition_probability)
    # print('emission_probability',emission_probability)
    return lis
#
State_File ='./dev_set/State_File'
Symbol_File='./dev_set/Symbol_File'
Query_File ='./dev_set/Query_File'

# State_File ='./toy_example/State_File'
# Symbol_File='./toy_example/Symbol_File'
# Query_File ='./toy_example/Query_File'
viterbi_result =viterbi_algorithm(State_File, Symbol_File, Query_File)
for row in viterbi_result:
    print(row)


# Question 2
def top_k_viterbi(State_File, Symbol_File, Query_File, k): # do not change the heading of the function
    pass # Replace this line with your implementation...


# Question 3 + Bonus
def advanced_decoding(State_File, Symbol_File, Query_File): # do not change the heading of the function
    pass # Replace this line with your implementation...
