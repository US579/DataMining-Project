# DataMining-Project


HMM decription
-----------
![image text](https://github.com/US579/DataMining-Project/blob/master/image/HMM.png)

the blue line represent the  initial probability which can be deemed as equivalent to transition probabilities from the BEGIN state to all the hidden state

So, we caculate as 

```
for s in states[:-2]:
    transition_probability[len(states)-2][states.index(s)])
```

the red line represent its emission probability from state after smoothing is 

<a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{n(i,j)&plus;1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{n(i,j)+1}{n(i)+M+1}" /></a>

If the symbol is an unknown symbol, its emission probability from state after smoothing is

<a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\frac{1}{n(i)&plus;M&plus;1}" title="B[i,j]=\frac{1}{n(i)+M+1}" /></a>
