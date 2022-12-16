import os

from collections import Counter, ChainMap, defaultdict, deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

def readmap():
    map = {}
    for line in read_input_lines():
        fromnode = line.split()[1]
        flow = int(line.split("rate=")[1].split(";")[0])
        outnodes = line.split("valves ")[-1].split(", ")
        map[fromnode] = (flow, outnodes)

    return map

def part_a():
    """each state is defined by which valves are open the current pos and the current t
       - we dont open flow rate 0s
       - as a possible optimization we could cut states with the same pos and fewer valves open than another state and t<state t"""
    map = readmap()
    states = {("AA", tuple(), 0) : 0} # state -> score

    current_states = {("AA", tuple(), 0)}
    next_states = set()
    for t in range(30):
        for node, opened, _ in current_states:
            flow, nextnodes = map[node]
            if (not node in opened) and (flow > 0):
                next_state = (node, tuple(sorted(opened + (node,))), t+1)
                next_score = states[(node,opened, t)] + flow * (30 - (t + 1))
                if next_score > (states.get(next_state) or -1):
                    states[next_state] = next_score
                    next_states.add(next_state)
            for nextnode in nextnodes:
                next_state = (nextnode, opened, t + 1)
                next_score = states[(node, opened, t)]
                if next_score > (states.get(next_state) or -1):
                    states[next_state] = next_score
                    next_states.add(next_state)
        current_states = next_states
        next_states = set()
        #print([(s, states[s]) for s in current_states])
        #if t == 5:
        #    break
    print(max(states.values()))


def part_b():
    """each state is defined by which valves are open the current pos (2x) and the current t
       - we dont open flow rate 0s
       - as a possible optimization we could cut states with the same pos and fewer valves open than another state and t<state t"""


    def get_max_score(state):
        altstate = (state[0][::-1],*state[1:])
        maxscore = -1
        maxscore =  states[state] if state in states and states[state] > maxscore else maxscore
        maxscore =  states[altstate] if altstate in states and states[altstate] > maxscore else maxscore
        return maxscore

    def filter_states(nextstates):
        """we greedily only retain the 20k states with the best score"""
        return set(sorted(list(nextstates), key= lambda x: states[x], reverse= True)[:20000])

    map = readmap()
    states = {(("AA", "AA"), tuple(), 0): 0}  # state -> score

    current_states = {(("AA", "AA"), tuple(), 0)}
    next_states = set()
    for t in range(26 * 2):
        posix = t % 2 #0 = me, 1 = elephant
        for nodes, opened, _ in current_states:
            node = nodes[posix]
            flow, nextnodes = map[node]
            if (not node in opened) and (flow > 0):
                next_state = (nodes, tuple(sorted(opened + (node,))), t + 1)
                next_score = states[(nodes, opened, t)] + flow * (26 - (t//2 + 1))
                if next_score > get_max_score(next_state):
                    states[next_state] = next_score
                    next_states.add(next_state)
            for nextnode in nextnodes:
                nextnodes = tuple([node if i != posix else nextnode for i, node in enumerate(nodes) ])
                next_state = (nextnodes, opened, t + 1)
                next_score = states[(nodes, opened, t)]
                if next_score > get_max_score(next_state):
                    states[next_state] = next_score
                    next_states.add(next_state)
        current_states = filter_states(next_states)
        next_states = set()
        print(t, len(current_states))
    print(max(states.values()))

part_b()
