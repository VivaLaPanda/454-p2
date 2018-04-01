from queue import *

#read in the file, line by line
#first line is n and k. n is the number of rows, k is the number of columns
#init 2d array[n][k]
#get line, fill second array



def main():

    file1 = open("dfa1.txt", "r")
    file2 = open("dfa2.txt", "r")
    d1 = file1.readlines()
    d2 = file2.readlines()
    #print(d1)
    #print(d2)

    d1f = d1[1].split()
    for k in range(len(d1f)):
        d1f[k] = int(d1f[k])
    words = d1[0].split()

    d1n = int(words[0])
    d1k = int(words[1])

    print(d1f)
    print(d1n)
    print(d1k)
    dfa1 = []

    for i in range(2,d1n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(d1k):
            ts.append(int(d1[i].split()[j]))
        dfa1.append(ts)

    print(dfa1)




    f = d2[1].split()
    for k in range(len(f)):
        f[k] = int(f[k])
    words = d2[0].split()

    n = int(words[0])
    k = int(words[1])

    print(f)
    print(n)
    print(k)
    dfa2 = []
    for i in range(2,n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(k):
            ts.append(int(d2[i].split()[j]))
        dfa2.append(ts)

    print(dfa2)

    Q = Queue()

    map = []
    map.append([0,0])
    node = []
    dfa3 = []
    Q.put(map[0])
    while (~Q.empty()):
        node = Q.get() # node = [x, y]

        # 0 = first dfa
        # 1 = second dfa
        tempNode1 = []
        tempNode1 = dfa1[node[0]]
        tempNode2 = []
        tempNode2 = dfa2[node[1]]







main()
