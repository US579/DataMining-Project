# DataMining-Project


HMM decription
-----------
![image text](https://github.com/US579/DataMining-Project/blob/master/image/HMM.png)

### 1.Initial Probilities 

The blue line represent the  initial probability (Pi) which can be deemed as equivalent to transition probabilities from the BEGIN state to all the hidden state

So, we caculate as 

```
for s in states[:-2]:
    transition_probability[len(states)-2][states.index(s)])
```

### 2.Emission Probilities  

The red line represent its emission probability from state after smoothing is 

<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{n(i,j)+1}{n(i)+M+1}" /></a></div>

If the symbol is an unknown symbol, its emission probability from state after smoothing is

<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{1}{n(i)+M+1}" /></a></div>

```
for i in range(1,len(obs)):
    for cur in range(len(states[:-2])):
                #if there is no emission from states `cur` to observation `sym.index(obs[i])`(this is the index in the symbol list),we us add one smoothing (in case it is 0)
                if str(cur)+'-'+str(sym.index(obs[i])) not in emission_probability:
                    emission_rate = 1.0 / (dic_distance[cur] + n2 +1)
                else:
                #otherwise i will use the formula below
                    emission_rate = emission_probability[str(cur)+'-'+str(sym.index(obs[i]))]
```

### 2.Transition Probilities  

The black line represent the transition probilities transfer the states from on to another 

```
for i in range(n1):
    for j in range(n1):
        transition_probability[i][j] = (float(distance[i][j])+1) / (sum(distance[i])+n1-1)
```
the number of state_i transfer to state_j divide by the total number of transfering state_j to any states , i also use add-1 smoothing here

### 3.Viterbi Algorithm

for HMM, the most useful function is to find the most likely hddien sequence according to its observation, and we can describe as below 
```
observations ：we observed phenomenon sequence
states ：all the possible hidden states
start_probability ：the initial probilities of each hidden states
transition_probability ：the probility of transfering from one hidden states to another
emission_probability ：the probility of some hidden states emit some observed phenomenon 
```
If you use the brute-force method to exhaust all possible state sequences and compare their probability values, the time complexity is O(n^m), obviously , this is unacceptable when we want to find a long sequnce whit large dataset, however, we candecrease its time complexity by using Viterbi Algorithemwe can consider this probelm as dynamic programming , the last_state is the probability of each implicit state corresponding to the previous observed phenomenon, and curr_pro is theprobability of each implicit state corresponding to the currentobserved phenomenon. Solving cur_pro actually depends only on last_state, this is core thinking of Vitberi Algorithem.




## Author

WANZE LIU


