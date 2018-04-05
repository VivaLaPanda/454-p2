from queue import *

#read in the file, line by line
#first line is n and k. n is the number of rows, k is the number of columns
#init 2d array[n][k]
#get line, fill second array



def main():

    #Open files
    file1 = open("dfa1.txt", "r")
    file2 = open("dfa2.txt", "r")
    d1 = file1.readlines()
    d2 = file2.readlines()


    #create our first DFA
    d1f = d1[1].split()
    for k in range(len(d1f)):
        d1f[k] = int(d1f[k])
    words = d1[0].split()

    d1n = int(words[0])
    d1k = int(words[1])

    print(d1f)
    #print(d1n)
    #print(d1k)
    dfa1 = []

    for i in range(2,d1n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(d1k):
            ts.append(int(d1[i].split()[j]))
        dfa1.append(ts)

    #print(dfa1)


    #create our seconed DFA

    f = d2[1].split()
    for k in range(len(f)):
        f[k] = int(f[k])
    words = d2[0].split()

    n = int(words[0])
    k = int(words[1])

    print(f)
    #print(n)
    #print(k)
    dfa2 = []
    for i in range(2,n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(k):
            ts.append(int(d2[i].split()[j]))
        dfa2.append(ts)

    #print(dfa2)


    #Build dour third DFA
    Q = Queue()

    fin_state = []
    map = []
    map.append([0,0])
    dfa3 = []

    Q.put(map[0])
    while (not Q.empty()):
        node = Q.get() # node = [x, y]
        print("queue size: ", Q.qsize())
        # 0 = first dfa
        # 1 = second dfa

        tempNode1 = dfa1[node[0]]
        tempNode2 = dfa2[node[1]]
        for i in range(k):
            index = len(map)
            newNode = []
            insert = True
            newNode.append(tempNode1[i])
            newNode.append(tempNode2[i])
            for j in range(len(map)):
            # if node isnt in the map
                if map[j] == newNode:
                    index = j
                    insert = False

            if insert:
                Q.put(newNode)
                dfa3.append(index)
                map.append(newNode)
                print("inserting node: ", newNode)
            else:
                dfa3.append(index)

           #find ending states, a little messy but it works
            for f1i in range(len(d1f)):
                for f2i in range(len(f)):
                    if tempNode1[i]== d1f[f1i] and tempNode2 [i] == f[f2i]:
                        set = True
                        for idx in range(len(fin_state)):
                           if fin_state[idx] == index:
                               set = False
                        if set:
                            fin_state.append(index)



    print ("map:  ",map)
    print("dfa3: ", dfa3)
    print("fin states: ", fin_state)

    #output third dfa
    f = open('dfa3.txt', 'w')
    pretext = str(len(map))+ " " + str(k)
    print(pretext)
    f.write(pretext)
    f.write("\n")
    #output finish states, formated semi nicely
    for idx in range(len(fin_state)):
        if idx != len(fin_state)-1:
            fin = str(fin_state[idx])+ " "
        else:
            fin = str(fin_state[idx])
        f.write(fin)

    x = 0

    for _ in range(len(dfa3)//k):
        f.write("\n")
        for y in range(k):
            print(dfa3[x+y],end=" ")
            f.write(str(dfa3[x+y]))
            if y+1 != k:
                f.write(" ")
        print()

        x += k








main()
