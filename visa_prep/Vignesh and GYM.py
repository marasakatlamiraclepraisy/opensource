gym_cost, trainer_cost, total_budget = map(int, input().split())
if gym_cost + trainer_cost <= total_budget:
    print(2)
elif gym_cost <= total_budget:
    print(1)
else:
    print(0)
