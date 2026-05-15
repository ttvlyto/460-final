# The Torchbearer

**Student Name:** ___________________________
**Student ID:** ___________________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _A single shortest path is not enough, because you need to collect all relics before leaving the dungeon. Therefore we are not looking for the shortest path to the exit, but the shortest path while collecting all relics._

- **What decision remains after all inter-location costs are known:**
  _Once all interlocations are known, you must then decided in what order to traverse the path to reduce the minimum number of edges while collecting all relics._

- **Why this requires a search over orders (one sentence):**
  _We must search over orders because we can collect the relics in any order, meaning that we must see which order is the most optimal to collect said relics._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _Start node_| _Because every problems starts here and see the cheapest cost to each relic_|
| _Relic node_| _Because every relic needs to be reached, and you cannot end at a relic, so you can only go to another relic or T_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name |Hashtable |
| What the keys represent |Using 2 keys, you could express the source node and the next travelled to |
| What the values represent |value would represent the cost of travelling to from source node to second key |
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible | Since we are using keys, there is no need to check individual buckets, we can jump straight to bucket|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _You would  have to run it for V - 1 times, where n is the number of nodes in the graph. You would need to run it on all sources nodes._
- **Cost per run:** _O((V+E) log V)_
- **Total complexity:** _(O(((V + E) log V))(V-1))_
- **Justification (one line):** _Dijkstras alone will cost (O((V + E) log V)), and it must be run for every source node. This means that the only node that doesnt get dijkstras performed on it would be hence V - 1._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _For finalized nodes, the value of dict[v] will contain the shortest path from a given source._

- **For nodes not yet finalized (not in S):**
  _For unfinalized node, dict[v] will hold the current shortest path that has been found, but there could exist a true shortest path._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _The heap must not be empty and the distance from source to itself must be 0._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _This allows us to skip stale entries, and avoid recomputing paths that are clearly not going to produce shorter paths._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The heap will be empty and all entries in dict will hold the true shortest path from source to every other node._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

I will be using the following graph, a variation of graph_1
 graph = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 5), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }


- **The failure mode:** _This example fails because when using a purely greedy implementation, would take 'B' first since its the locally optimal choice, but then forces you but it forces you to incur 5, right after with no way to back track._
- **Counter-example setup:** _The real optimal answer would be S->D->C->B->T. with a cost of 5. Picking a not optimal choice of 'D' first, allows us to avoid the heavy penalty you would incur from taking the 'B' path first._
- **What greedy picks:** _Greedy picks after 'S', greedy would pick 'B' first, as it the cheapest out of the other sources._
- **What optimal picks:** _Optimal picks 'D' first since we incur a smaller penalty first, but can avoid taking a heavy penalty later._
- **Why greedy loses:** _Greedy loses because we go with the locally optimal choice 'B', however for a problem like this, you would bneed to explore other paths before committing to one._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algorithm must explore all the possible paths. Since there is a limited number of relics, you could get the permutation of relic orders, and traverse the graph that way._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
