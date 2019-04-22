# -*- codeing:utf-8 -*-
import math
# Question 1
def viterbi_algorithm(State_File, Symbol_File, Query_File): # do not change the heading of the function
    states = []
    sym = []
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
    lis = []
    for obs in obs:
        lis.append(viterbi(states,obs,transition_probability,emission_probability,sym,distance2,n2))
    return lis

def viterbi(states,obs,transition_probability,emission_probability,sym,distance2,n2):
    path = {s:[] for s in states}
    curr_pro = {}
    for s in states[:-2]:
        curr_pro[s] = transition_probability[len(states)-2][states.index(s)]*emission_probability[states.index(s)][sym.index(obs[0])]
    for i in range(1,len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for cur in range(len(states[:-2])):
            try:
                (max_pr,last_state) = max([(last_pro[k] * transition_probability[states.index(k)][cur]*
                                       emission_probability[cur][sym.index(obs[i])], k) for k in states[:3]])
            except:
                (max_pr,last_state) = max([(last_pro[k] * transition_probability[states.index(k)][cur] *
                                        (1/(sum(distance2[cur])+n2 +1)) , k) for k in states[:3]])
            curr_pro[states[cur]] = max_pr
            path[states[cur]].append(last_state)
    for i in states[:-2]:
        curr_pro[i] = curr_pro[i] * transition_probability[states.index(i)][len(states)-1]
    max_pr=max(curr_pro,key=lambda x:curr_pro[x])
    lis = [states[-1],max_pr]
    for num in range(len(path[max_pr])-1,-1,-1):
        lis.append(path[lis[-1]][num])
    lis.append(states[-2])
    lis = [states.index(ele) for ele in lis[::-1]]
    lis.append(math.log(curr_pro[max_pr]))
    # print('obs',obs)
    # print('states',states)
    # print('sym',sym)
    # print('transition_probability',transition_probability)
    # print('emission_probability',emission_probability)
    return lis


State_File ='./toy_example/State_File'
Symbol_File='./toy_example/Symbol_File'
Query_File ='./toy_example/Query_File'
viterbi_result =viterbi_algorithm(State_File, Symbol_File, Query_File)
for row in viterbi_result:
    print(row)


# Question 2
def top_k_viterbi(State_File, Symbol_File, Query_File, k): # do not change the heading of the function
    pass # Replace this line with your implementation...


# Question 3 + Bonus
def advanced_decoding(State_File, Symbol_File, Query_File): # do not change the heading of the function
    pass # Replace this line with your implementation...
