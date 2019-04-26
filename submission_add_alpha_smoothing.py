# -*- codeing:utf-8 -*-
import math
import numpy as np
import pandas as pd
import heapq

###########################################################################################################
# Viterbi Algorithm for HMM
# dp, time complexity O(mn^2), m is the length of sequence of observation, n is the number of hidden states
##########################################################################################################

# Question 1
def viterbi_algorithm(State_File, Symbol_File, Query_File): # do not change the heading of the function
    lis = []
    states, obs, transition_probability, emission_probability, sym, n2, dic_distance,alpha =\
        file_reader(State_File, Symbol_File, Query_File)
    for obs in obs:
        lis.append(viterbi(states,obs,transition_probability,emission_probability,sym,n2,dic_distance,alpha))
    return lis

def file_reader(State_File, Symbol_File, Query_File):
    states = []
    sym = []
    alpha = 0.2
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
                    transition_probability[i][j] = (float(distance[i][j])+alpha) / (sum(distance[i])+alpha*(n1-1))

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
        emission_probability[i[0]+'-'+i[1]] =(alpha*(float(i[2])+1)) / (dic_distance[int(i[0])]+alpha*(n2 +1))
    with open(Query_File) as f3:
        n3 = f3.readlines()
        obs = [x.strip().split() for x in n3]
    obs = split(obs)
    return states, obs, transition_probability, emission_probability, sym, n2, dic_distance,alpha


def split(obs):
    flag = [',','(',')','/','-']
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
            if len(v) != 1 and '/' in v:
                lis_sym.extend([v[:v.index('/')],'/',v[v.index('/')+1:]])
                continue
            if len(v) != 1 and '-' in v:
                lis_sym.extend([v[:v.index('-')],'-',v[v.index('-')+1:]])
                continue
            lis_sym.append(v)
        lis_s.append(lis_sym)
        lis_sym = []
    return lis_s

def viterbi(states,obs,transition_probability,emission_probability,sym,n2,dic_distance,alpha):
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
                    emission_rate = alpha / (dic_distance[cur] +alpha*(n2 +1))
                else:
                    emission_rate = emission_probability[str(cur)+'-'+str(sym.index(obs[i]))]
                (max_pr,last_state) = max([(last_pro[k]+math.log(transition_probability[states.index(k)][cur])+
                                            math.log(emission_rate), k) for k in states[:-2]])
            except:
                (max_pr,last_state) = max([(last_pro[k] +math.log(transition_probability[states.index(k)][cur])+
                                            math.log (alpha/(dic_distance[cur]+alpha*(n2 +1))), k) for k in states[:-2]])
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
    return lis



# Question 2
def text_processing(State_File, Symbol_File, Query_File):
    states = []
    sym = []
    with open(State_File) as f1:
        n1 = int(f1.readline())
        distance = np.zeros((n1, n1))
        transition_probability = np.zeros((n1, n1))
        for i in range(n1):
            states.append(f1.readline().strip())
        st = f1.readlines()
        lis = [j.strip().split() for j in st]
        for i in lis:
            distance[int(i[0])][int(i[1])] = int(i[2])
        for i in range(n1):
            for j in range(n1):
                transition_probability[i][j] = (float(distance[i][j]) + 1) / (sum(distance[i]) + n1 - 1)

    with open(Symbol_File) as f2:
        n2 = int(f2.readline())
        emission_probability = dict()
        distance2 = {}
        for i in range(n2):
            sym.append(f2.readline().strip())
        st2 = f2.readlines()
        lis2 = [j.strip().split() for j in st2]

    n_label = dict()
    for i in lis2:
        if int(i[0]) not in n_label:
            n_label[int(i[0])] = 1
        else:
            n_label[int(i[0])] += 1

    state_map = dict()
    for num, words in enumerate(sym):
        state_map[words] = num

    for i in lis2:
        distance2[i[0] + '-' + i[1]] = int(i[2])
    dic_distance = {}
    for i in lis2:
        if int(i[0]) not in dic_distance:
            dic_distance[int(i[0])] = int(i[2])
        else:
            dic_distance[int(i[0])] += int(i[2])
    for i in lis2:
        emission_probability[(int(i[0]), int(i[1]))] = (float(i[2]) + 1) / (dic_distance[int(i[0])] + n2 + 1)

    with open(Query_File) as f3:
        n3 = f3.readlines()
        obs = [x.strip().split() for x in n3]
    obs = split(obs)
    pi = list()
    for s in states[:-2]:
        pi.append(transition_probability[len(states) - 2][states.index(s)])
    return state_map, transition_probability, emission_probability, obs, pi, n1, n2, dic_distance

def array_init(observation_count, state_count, top_k, emission_pro, observation, pi, dic_distance, n2):
    terminal_pro = np.zeros((observation_count, state_count, top_k))
    arg_max_pro = np.zeros((observation_count, state_count, top_k), int)
    rank = np.zeros((observation_count, state_count, top_k), int)
    for i in range(state_count):
        if observation[0] != -1 and (i, observation[0]) in emission_pro.keys():
            terminal_pro[0, i, 0] = pi[i] * emission_pro[(i, observation[0])]
        else:
            terminal_pro[0, i, 0] = pi[i] * (1 / (dic_distance[i] + n2 + 1))

        arg_max_pro[0, i, 0] = i
        for k in range(1, top_k):
            terminal_pro[0, i, k] = 0.0
            arg_max_pro[0, i, k] = i

    return terminal_pro, arg_max_pro, rank

# Question 2
def top_k_viterbi(State_File, Symbol_File, Query_File, k):  # do not change the heading of the function
    if k == 1:
        return viterbi_algorithm(State_File, Symbol_File, Query_File)

    state_map, transition_pro, emission_pro, obs, pi, n1, n2, dic_distance = \
        text_processing(State_File, Symbol_File, Query_File)
    # print(state_map, '\n', transition_pro, '\n', emission_pro, '\n',  pi)

    pi = np.array(pi)
    transition_pro = np.array(transition_pro)

    all_result = list()
    for query in obs:
        observation_query = list()
        for words in query:
            if words in state_map.keys():
                observation_query.append(state_map[words])
            else:
                observation_query.append(-1)

        path, probability = top_k_algorithm(pi, transition_pro, emission_pro, observation_query, k, n1, n2,
                                            dic_distance)

        result = list()
        for p in range(len(path)):
            sub_list = list()
            sub_list.extend([_ for _ in path[p]])
            sub_list.insert(0, n1 - 2)
            sub_list.append(n1 - 1)
            single_pro = np.log(probability[:, -1] * transition_pro[path[p][-1], n1 - 1])
            sub_list.append(single_pro[p])
            result.append(sub_list)
        all_result.extend(result)
    return all_result

def top_k_algorithm(pi, transmission_pro, emission_pro, observation, top_k, n1, n2, dic_distance):
    state_count = n1 - 2
    observation_count = np.shape(observation)[0]

    # top k cannot beyond all possibilities of paths
    if top_k > state_count ** observation_count:
        return False

    terminal_pro, arg_max_pro, rank = array_init(observation_count, state_count,
                                                 top_k, emission_pro, observation, pi, dic_distance, n2)

    for obs in range(1, observation_count):
        for curr_state in range(state_count):
            h = list()
            for prev_state in range(state_count):
                for k in range(top_k):
                    if observation[obs] != -1 and (curr_state, observation[obs]) in emission_pro.keys():
                        prob = terminal_pro[obs - 1, prev_state, k] * \
                               transmission_pro[prev_state, curr_state] * emission_pro[
                                   (curr_state, observation[obs])]
                    else:
                        prob = terminal_pro[obs - 1, prev_state, k] * \
                               transmission_pro[prev_state, curr_state] * (1 / (dic_distance[curr_state] + n2 + 1))
                    state = prev_state
                    heapq.heappush(h, (prob, state))
            h_sorted = [heapq.heappop(h) for _ in range(len(h))]
            h_sorted.reverse()
            path_rank_dict = dict()

            for k in range(0, top_k):
                terminal_pro[obs, curr_state, k] = h_sorted[k][0]
                arg_max_pro[obs, curr_state, k] = h_sorted[k][1]
                state = h_sorted[k][1]

                if state in path_rank_dict:
                    path_rank_dict[state] = path_rank_dict[state] + 1
                else:
                    path_rank_dict[state] = 0
                rank[obs, curr_state, k] = path_rank_dict[state]
    h = list()
    for curr_state in range(state_count):
        for k in range(top_k):
            prob = terminal_pro[observation_count - 1, curr_state, k]
            heapq.heappush(h, (prob, curr_state, k))

    h_sorted = [heapq.heappop(h) for i in range(len(h))]
    h_sorted.reverse()

    path = np.zeros((top_k, observation_count), int)
    path_probability = np.zeros((top_k, observation_count), float)

    for k in range(top_k):
        max_prob = h_sorted[k][0]
        state = h_sorted[k][1]
        top_k_rank = h_sorted[k][2]

        path_probability[k][-1] = max_prob
        path[k][-1] = state

        for obs in range(observation_count - 2, -1, -1):
            next_state = path[k][obs + 1]
            p = arg_max_pro[obs + 1][next_state][top_k_rank]
            path[k][obs] = p
            top_k_rank = rank[obs + 1][next_state][top_k_rank]

    return path, path_probability

# Question 3 + Bonus
def advanced_decoding(State_File, Symbol_File, Query_File): # do not change the heading of the function
    pass # Replace this line with your implementation...



if __name__ == "__main__":
    State_File ='./dev_set/State_File'
    Symbol_File='./dev_set/Symbol_File'
    Query_File ='./dev_set/Query_File'

    # State_File = './toy_example/State_File'
    # Symbol_File = './toy_example/Symbol_File'
    # Query_File = './toy_example/Query_File'
    print("====================The implict sequence ====================")
    viterbi_result = viterbi_algorithm(State_File, Symbol_File, Query_File)
    for row in viterbi_result:
        print(row)
    # print("====================Top K Viterbi====================")
    # top_result = top_k_viterbi(State_File, Symbol_File, Query_File, 4)
    # for row in top_result:
    #     print(row)
