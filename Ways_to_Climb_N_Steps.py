
# N denotes the number of steps.
# Steps can be taken in increments of 1 or 2.
# How many unique ways can you reach the top?

n = int(input("Please input the number of steps you would like to climb: "))
seed0 = 1
seed1 = 1
sum = 0

for i in range(0, n - 1):
    hold = seed1
    seed1 = seed1 + seed0  # After first loop Seed1 = 1. Second loop seed1 = 2.
    seed0 = hold # After first loop seed0 = 1. 
    
print(f"There are exactly {seed1} ways to climb {n} steps")