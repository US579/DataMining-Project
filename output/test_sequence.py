def test_sequence(output,answer):
    with open(output) as f1:
        a = f1.readlines()
        lis = []
        for i in a:
            lis.append(i.split(', '))
            lis[-1] = [lis[-1][0][1:]] + lis[-1][1:-1] +[lis[-1][-1][:-2]]

    lis2 = []
    with open(answer) as f2:
        b = f2.readlines()
        for i in b:
            lis2.append(i.split())


    for v in range(len(lis)):
        print('{}  {}'.format(v+1,lis[v]))
        print('    {}'.format(lis2[v]))
        print()
        print()




output = '/Users/us579/Desktop/19S1/DataMining-Project/output.txt'
answer = '/Users/us579/Desktop/19S1/DataMining-Project/dev_set/Query_Label'
test_sequence(output,answer)
