"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Manuel Jimenez
Student ID:   828131233

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """
    Why a single shortest-path run from S is not enough: A single shortest path is not enough, because you need to collect all relics before leaving the dungeon. Therefore we are not looking for the shortest path to the exit, but the shortest path while collecting all relics.

    What decision remains after all inter-location costs are known: Once all interlocations are known, you must then decided in what order to traverse the path to reduce the minimum number of edges while collecting all relics.

    Why this requires a search over orders (one sentence): We must search over orders because we can collect the relics in any order, meaning that we must see which order is the most optimal to collect said relics.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """

    source = []
    source.append(spawn) #add spawn and all relics to source, pretty self explanatory
    for i in range(len(relics)):
        source.append(relics[i])

    return source





def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """

    dist = {node: float('inf') for node in graph} #create dict for every node in graph, and init to inf
    dist[source] = 0 #set source node distance to 0
    heap = [] #init heap and add spawn node immediately
    heapq.heappush(heap, (0,source))


    while heap: #loop until heap is empty
        smallest_dist, smallest_elem = heapq.heappop(heap) #pop off the heap

        if smallest_dist > dist[smallest_elem]: #skip elements that wont beat smallest distance already calulated
            continue

        length = len(graph[smallest_elem])
        for i in range(length): #discover edges
            t = (graph[smallest_elem][i][1], graph[smallest_elem][i][0]) # create temp tuple for pushing into heap
            new_dist = dist[smallest_elem] + t[0]
            if new_dist < dist[t[1]]:  
                 heapq.heappush(heap, t) #push onto heap if the new distance results in smaller distance
                 dist[t[1]] = new_dist


    return dist



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    distances = {node: {nodes: float('inf') for nodes in graph} for node in sources} #nested dict, with as required to return, and set everything to inf

    length = len(sources) 
    for i in range(length): 
        compute = run_dijkstra(graph, sources[i]) #do dijktras for each source node

        for key in compute:
            distances[sources[i]][key] = compute[key] # add all entries for current source to respective place in lookup table, dist[u][v] for lookups

    return distances

# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    Part 3a: What the Invariant Means
    Two bullets: one for finalized nodes, one for non-finalized nodes. Do not copy the invariant text from the spec.

    For nodes already finalized (in S): For finalized nodes, the value of dict[v] will contain the shortest path from a given source.

    For nodes not yet finalized (not in S): For unfinalized node, dict[v] will hold the current shortest path that has been found, but there could exist a true shortest path.

    Part 3b: Why Each Phase Holds
    One to two bullets per phase. Maintenance must mention nonnegative edge weights.

    Initialization : why the invariant holds before iteration 1: The heap must not be empty and the distance from source to itself must be 0.

    Maintenance : why finalizing the min-dist node is always correct: This allows us to skip stale entries, and avoid recomputing paths that are clearly not going to produce shorter paths.

    Termination : what the invariant guarantees when the algorithm ends: The heap will be empty and all entries in dict will hold the true shortest path from source to every other node.

    Part 3c: Why This Matters for the Route Planner
    One sentence connecting correct distances to correct routing decisions.
   
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
    Why Greedy Fails
    State the failure mode. Then give a concrete counter-example using specific node names or costs (you may use the illustration example from the spec). Three to five bullets.

    I will be using the following graph, a variation of graph_1 graph = { 'S': [('B', 1), ('C', 2), ('D', 2)], 'B': [('D', 5), ('T', 1)], 'C': [('B', 1), ('T', 1)], 'D': [('B', 1), ('C', 1)], 'T': [] }

    The failure mode: This example fails because when using a purely greedy implementation, would take 'B' first since its the locally optimal choice, but then forces you but it forces you to incur 5, right after with no way to back track.
    Counter-example setup: The real optimal answer would be S->D->C->B->T. with a cost of 5. Picking a not optimal choice of 'D' first, allows us to avoid the heavy penalty you would incur from taking the 'B' path first.
    What greedy picks: Greedy picks after 'S', greedy would pick 'B' first, as it the cheapest out of the other sources.
    What optimal picks: Optimal picks 'D' first since we incur a smaller penalty first, but can avoid taking a heavy penalty later.
    Why greedy loses: Greedy loses because we go with the locally optimal choice 'B', however for a problem like this, you would bneed to explore other paths before committing to one.
    What the Algorithm Must Explore
    One bullet. Must use the word "order."

    The algorithm must explore all the possible paths. Since there is a limited number of relics, you could get the permutation of relic orders, and traverse the graph that way.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """


    best = [float('inf'), []] #hold the best current found cost, along with respective nodes that made up the route
    cost_so_far = 0
    curr_loc = spawn #set current to spawn node to begin the iteration
    remaining_relics = relics #all relics are remaining before recursion
    relics_visited_order = [] # no relics are visited before recursion

    _explore(dist_table, curr_loc, remaining_relics, relics_visited_order, cost_so_far, exit_node, best)

    return tuple(best) # cast to tuple type as expected







def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    length = len(relics_remaining)

    if length == 0: # if no more relics, then we are at the end
        if dist_table[current_loc][exit_node]: # check if there exist a path from current key to exit node
            if cost_so_far < best[0]: # check if the cost is better than our current best
                best[0] = cost_so_far + dist_table[current_loc][exit_node] # newly found cost becomes our best
                best[1] = list(relics_visited_order) # make copy of list order for visted relics
                return
        
        return 
    elif cost_so_far > best[0]: # pruning step, if the current path incurred a higher cost than our best, then its no longer worth following this path
        return
    else:
        for relic in list(relics_remaining): # loop over relics remaining, but use shallow copy 
            relics_remaining.remove(relic)
            relics_visited_order.append(relic) # remove relic from remaining and mark as visited

            cost = cost_so_far + dist_table[current_loc][relic] # update cost
            _explore(dist_table, relic, relics_remaining, relics_visited_order, cost, exit_node, best) # use recursion to visit the next node
            # backtrack step, if we return from above, then we can remove from visited and add back to remaing 
            # allows for us to uncommit from a path and try a new one
            relics_visited_order.pop()
            relics_remaining.append(relic)


        
# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    distances = precompute_distances(graph, spawn, relics, exit_node)
    optimal = find_optimal_route(distances, spawn, relics, exit_node)

    
    return optimal


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()




