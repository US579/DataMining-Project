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

<a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{n(i,j)+1}{n(i)+M+1}" /></a>

If the symbol is an unknown symbol, its emission probability from state after smoothing is

<a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{1}{n(i)+M+1}" /></a>

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



