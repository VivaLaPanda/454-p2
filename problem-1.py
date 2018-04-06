import sys

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

def main():
    print(traverseDFA(2000, 1000))

main()
