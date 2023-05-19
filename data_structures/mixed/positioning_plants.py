def positioning_plants(costs):
    return _positioning_plants(costs, pos=0, last_plant=None, memo={})

def _positioning_plants(costs, pos, last_plant, memo):
    key = ( pos, last_plant )
    if key in memo:
        return memo[key]
    
    if pos >= len(costs):
        return 0
    
    min_cost = float('inf')
    for plant, cost in enumerate(costs[pos]):
        if last_plant != plant:
            curr_cost = cost + _positioning_plants(costs, pos+1, last_plant=plant, memo=memo)
            if curr_cost < min_cost:
                min_cost = curr_cost
    memo[key] = min_cost
    return memo[key]

costs = [
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
] # -> 7, by doing 4 + 1 + 2.

costs_2 = [
  [12, 14, 5],
  [6, 3, 2],
  [4, 2, 7],
  [4, 8, 4],
  [1, 13, 5],
  [8, 6, 7],
] # -> 23

print(f"{positioning_plants(costs) = }")
print(f"{positioning_plants(costs_2) = }")
