# Development Log – The Torchbearer

**Student Name:** Manuel Jimenez
**Student ID:** 828131233

---

## Entry 1 – [5/11/26]: Initial Plan

_First I plan to use dijkstras to find the shortest path to every node. Once that is computer I plan on using a dynamic programming approach for saving time on calculations to other shortest nodes. After that I will work on finding an optimal route. This is where I think the precomputed distances will come in handy. You should then be able to find an optimal route using the recursive _explore funtion._

---

## Entry 2 – [5/13/26]: [Distance table / precomputation]

_Here I had wrongly assumed that only direct edges should go into the precomputed distances table. At first I thought this was an extension of the adjacenty table. This meant that there would be no entries like dict[S][T]. That was not the case, because dijktras is solving to see what the shortest path to reach possible node. Once I had figured this out, I was able to adjust the precompute table and add entries for all source nodes and exit node. This is necessary because the table then can tell you whether a past exist between two nodes, and when a node cannot be reach it will be marked as infinity. so this helped for finding paths that had no escape._

---

## Entry 3 – [5/14/26]: [_explore list issues]

_During the recursive step in explore, I would keep passing the original list and the orignal count over to the recursive funciton call. I didnt realize that by doing this, One I was muting the list incorrectly, meaning that during each recursive call, i would be grabbing orignal list and very quickly would run out of "remaining relics". I was under the impression that each recursive call would be free to do what it wants with said list but thats not the case all. I learned that the list was being shared with each recursive call being made, and in order to circumvent this, I had to create a shallow copy, and use the shallow copy for each respective recursive call. Something similar with cost variable, i had multiple recursive functions adding to the cost variable that i was getting answers that werent even possible.  Instead of a shallow copy, I ended up having to create a local variable inside the loop for each recursive call._

---

## Entry 4 – [5/14/26]: Post-Implementation Reflection

_I did not give myself as much time as I wanted to for completing this assignment, so im not entirely sure if my pruning technique was entirely correct. I figured you could save time by stopping when a path is already longer than our current best, since at that point it would no longer be possible to beat it. And it serves no use for us go along the path any further. It seemed like a basic but effective way cut down on searching paths, but I thought there could be a more elegant way of doing so. But my solution at least seemed practical._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 45 mins|
| Part 2: Precomputation Design | 2 hour 15 mins|
| Part 3: Algorithm Correctness | 1 hour 15 mins |
| Part 4: Search Design | 1 hour 15 mins |
| Part 5: State and Search Space | ~ 3-4 hours ... i lost count... |
| Part 6: Pruning | 2 hours |
| Part 7: Implementation | 30 mins |
| README and DEVLOG writing | 2 hours |
| **Total** | ~13 hours |
