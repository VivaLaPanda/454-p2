import sys

# Table is laid out like
# 0-9 as columns
# row for 0-2k
# each cell has K + current state and s


def genDFA(k):
    dfa = [[[]]]
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

