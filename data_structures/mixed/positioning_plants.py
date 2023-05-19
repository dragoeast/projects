def positioning_plants(costs):
  return _positioning_plants(costs, pos=0, last_plant=None)

def _positioning_plants(costs, pos, last_plant):
  if pos >= len(costs):
    return 0
  
  min_cost = float('inf')
  for cost in costs[pos]:
    for plant in range(cost[pos]):
      if plant is not last_plan:
        curr_cost = last_plant + _positioning_plants(costs, pos+1, last_plant=plant)
        if curr_cost < min_cost:
          min_cost = curr_cost
  return min_cost