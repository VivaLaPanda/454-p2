import sys
import subprocess
from queue import *

### P1 BEGIN
# Table is laid out like
# 0-9 as columns
# row for 0-2k
# each cell has K + current state and s


def genDFA(k):
    dfa = [[[] for j in range(10)] for i in range(k*2)]
    for state in range(k):
        dfa[state] = [[], [], [], [], [], [], [], [], [], []]
        for digit in range(10):
            dfa[state][digit].append(state + k) # transition to second DFA
            dfa[state][digit].append((state * 10 + digit) % k) # regular transition

    for state in range(2 * k)[k:]:
        dfa[state] = [[], [], [], [], [], [], [], [], [], []]
        for digit in range(10):
            dfa[state][digit].append((state * 10 + digit) % k) # regular transition

    return dfa


def traverseDFA(digitString, k):
    nfa = genDFA(k)
    print("Printing NFA:\n")
    print(nfa)
    print("\n\n")
    currentStates = [0]

    for character in str(digitString):
        nextStates = []
        for state in currentStates:
            nextStates.extend(nfa[state][int(character)])
        currentStates.extend(nextStates)

    for state in currentStates[1:]:
        if (int(state) == 0):
            return False

    return True

### P1 END

### P2 BEGIN

def p2program(digitString):
    # run with python 2.7
    command = 'egrep'
    regex = '([a-z])\\1[a-z]*([a-z])\\2'
    print(regex)
    #f = '/usr/share/dict/words'
    f = digitString
    #f = 'problem-2.txt'
    cmd_list = [command, regex, f]
    #print(cmd_list)
    subprocess.call(cmd_list)


### P2 END
### P3 BEGIN


#read in the file, line by line
#first line is n and k. n is the number of rows, k is the number of columns
#init 2d array[n][k]
#get line, fill second array



def p3program():

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

    #print(d1f)

    dfa1 = []

    for i in range(2,d1n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(d1k):
            ts.append(int(d1[i].split()[j]))
        dfa1.append(ts)

    #create our seconed DFA

    f = d2[1].split()
    for k in range(len(f)):
        f[k] = int(f[k])
    words = d2[0].split()

    n = int(words[0])
    k = int(words[1])

    #print(f)
    #print(n)
    #print(k)
    dfa2 = []
    for i in range(2,n+2): #skip the first two rows which are not the dfa
        ts = []
        for j in range(k):
            ts.append(int(d2[i].split()[j]))
        dfa2.append(ts)

    #Build dour third DFA
    Q = Queue()

    fin_state = []
    map = []
    map.append([0,0])
    if d1f[0] == 0 and f[0] == 0:
        fin_state.append(0)

    dfa3 = []

    Q.put(map[0])
    while (not Q.empty()):
        node = Q.get() # node = [x, y]
        #print("queue size: ", Q.qsize())
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
                #print("inserting node: ", newNode)
                # find ending states, a little messy but it works
                for f1i in range(len(d1f)):
                    for f2i in range(len(f)):
                        if tempNode1[i] == d1f[f1i] and tempNode2[i] == f[f2i]:
                            #set = True
                            #for idx in range(len(fin_state)):
                                #if fin_state[idx] == index:
                                    #set = False
                            #if set:
                            fin_state.append(index)

            else:
                dfa3.append(index)

    #print ("map:  ",map)
    #print("dfa3: ", dfa3)
    #print("fin states: ", fin_state)

    #output third dfa
    f = open('dfa3.txt', 'w')
    pretext = str(len(map))+ " " + str(k)
    #print(pretext)
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
            #print(dfa3[x+y],end=" ")
            f.write(str(dfa3[x+y]))
            if y+1 != k:
                f.write(" ")
        #print()

        x += k

### P3 END

def main():
    print("CS454 P2 By Adrian Smith, Ryan Yu & Jeff B.-K.")
    p_num = input("select Problem 1, 2, or 3:")

    if p_num == "1":
        p1_k = int(input("Please input a k: "))
        digi_string = int(input("please input ints: "))
        print(traverseDFA(p1_k,digi_string))

    if p_num == "2":
        digi_string = input("please provide the name of a text file: ")
        p2program(digi_string)

    if p_num == "3":
        print("converting dfa1.txt and dfa2.txt into dfa3.txt")
        p3program()

main()