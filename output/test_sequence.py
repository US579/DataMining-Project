# -*- coding: utf-8 -*-
__author__ = 'US579'

def test_wrong_sequence_error(output,answer):
    '''
    output : sumbission.py output
             fromat    [24, 0, 1, 2, 3, 18, 4, 18, 5, 6, 25, -58.407178051467]

    answer : Query_Label file

    automatic compare 
    1  ['24', '0', '1', '2', '3', '18', '4', '18', '5', '6', '25']  11  <--this is length
       ['24', '10', '1', '2', '3', '18', '4', '18', '5', '6', '25']  11 


    2  ['24', '2', '3', '18', '4', '18', '5', '6', '25']  9
        ['24', '2', '3', '18', '4', '18', '5', '6', '25']  9


    3  ['24', '8', '9', '18', '4', '18', '5', '6', '25']  9
       ['24', '8', '9', '18', '4', '18', '5', '6', '25']  9


    4  ['24', '16', '0', '19', '1', '2', '3', '18', '4', '18', '5', '6', '25']  13
        ['24', '14', '14', '14', '1', '2', '3', '18', '4', '18', '5', '6', '25']  13


    5  ['24', '8', '8', '8', '9', '19', '1', '20', '1', '19', '1', '2', '18', '4', '18', '5', '6', '25']  18
        ['24', '14', '14', '14', '14', '14', '9', '23', '9', '19', '1', '2', '18', '4', '18', '5', '6', '25']  18


    6  ['24', '0', '19', '2', '3', '18', '4', '18', '5', '6', '25']  11
        ['24', '1', '19', '2', '3', '18', '4', '18', '5', '6', '25']  11


    7  ['24', '0', '19', '1', '2', '2', '3', '18', '4', '18', '5', '6', '25']  13
        ['24', '0', '19', '1', '2', '2', '3', '18', '4', '18', '5', '6', '25']  13

        etc......


    '''
    with open(output) as f1:
        a = f1.readlines()
        lis = []
        for i in a:
            lis.append(i.split(', '))
            lis[-1] = [lis[-1][0][1:]] + lis[-1][1:-1]

    lis2 = []
    with open(answer) as f2:
        b = f2.readlines()
        for i in b:
            lis2.append(i.split())

    num = 0
    for v in range(len(lis)):

        print('{}  {}  {}'.format(v+1,lis[v],len(lis[v])))
        print('    {}  {}'.format(lis2[v],len(lis2[v])))
        print()
        print()
        for k in range(len(lis[v])):
            if lis[v][k] != lis2[v][k]:
                num+= 1
    print("the total different number is: {}".format(num))





output = '/Users/us579/Desktop/19S1/DataMining-Project/output.txt'
answer = '/Users/us579/Desktop/19S1/DataMining-Project/dev_set/Query_Label'
test_wrong_sequence_error(output,answer)

'''
python3 test_sequence.py > compare.txt
'''
