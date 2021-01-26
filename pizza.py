pizzacount, team2, team3, team4 = [int(x) for x in input().split()]

ingredientcount = []
pizza = []

# reads input
for i in range(pizzacount):
    pizzalist = input().split()
    ingredientcount.append(int(pizzalist[0]))
    pizza.append(pizzalist[1:])

# need to handle when pizza less than 1

oteam4 = oteam3 = oteam2 = 0
# counts how many teams can get the orders
if (pizzacount // 4) > team4: 
    pizzacount = pizzacount - (4 * team4)
    oteam4 += team4
    # now check for remaining pizzas to distribute from team3
    if (pizzacount // 3) > team3:
        pizzacount = pizzacount - (3 * team3)
        oteam3 += team3
        # now remaining pizzas goes to team2
        if(pizzacount // 2) > team2:
            pizzacount = pizzacount - (2 * team2)
            oteam2 = team2
        elif (pizzacount // 2) > 0:
            oteam2 = pizzacount // 2
            pizzacount = pizzacount - (2 * oteam2)
    elif (pizzacount % 3) == 0:
        oteam3 = pizzacount // 3
        pizzacount = pizzacount - (3 * oteam3)
    elif (pizzacount % 3) == 1:
        oteam3 = (pizzacount // 3) - 1
        pizzacount = pizzacount - (3 * oteam3)
        if (pizzacount // 2) > team2:
            oteam3 += 1
            pizzacount -= 3
        else:
            oteam2 = pizzacount // 2
            pizzacount -= (2 * oteam2)
    elif (pizzacount % 3) == 2:
        oteam3 = pizzacount // 3
        pizzacount = pizzacount - (3 * oteam3)
        oteam2 = pizzacount // 2
elif (pizzacount % 4) == 0:
    oteam4 = pizzacount // 4
    pizzacount = pizzacount - (4 * oteam4)
elif (pizzacount % 4) == 1:
    oteam4 = (pizzacount // 4) - 1
    pizzacount = pizzacount - (4 * oteam4)
    if (team2 == 0 or team3 == 0):
        oteam4 += 1
        pizzacount -= 4
    else:
        oteam3 = oteam2 = 1 
        pizzacount = pizzacount - 5
elif (pizzacount % 4) == 2:
    oteam4 = pizzacount // 4
    pizzacount = pizzacount - (4 * oteam4)
    if (pizzacount // 2) <= team2:
        oteam2 = pizzacount // 2
        pizzacount = pizzacount - (2 * oteam2)
elif (pizzacount % 4) == 3:
    oteam4 = pizzacount // 4
    pizzacount = pizzacount - (4 * oteam4)
    if (pizzacount // 3) <= team3:
        oteam3 = pizzacount // 3
        pizzacount = pizzacount - (3 * oteam3)
    else:
        if (pizzacount // 2) <= team2:
            oteam2 = pizzacount // 2
            pizzacount = pizzacount - (2 * oteam2)

print(oteam2 + oteam3 + oteam4)

oteam4 *= 4
oteam3 *= 3
oteam2 *= 2

pizza4 = []
pizza3 = []
pizza2 = []

# max_index = ingredientcount.index(max(ingredientcount))

temp = ingredientcount[:]
temp2 = []
for i in range(3):
    if len(temp) == 0:
        break
    temp_max = temp.index(max(temp))

    for j in pizza[temp_max+i]:
        temp2.append(j)
    
    temp.pop(temp_max)

differences = []
for value in pizza:
    diff = 0
    for i in value:
        if i in temp2:
            diff += 1
    differences.append(diff)

count = 0
temp3 = pizza[:]

while True:  
    if len(ingredientcount) == 0:
        break
    max_index = differences.index(min(differences))

    if oteam4 > 0:
        oteam4 -= 1
        pizza4.append(pizza[max_index])
    elif oteam3 > 0:
        oteam3 -= 1
        pizza3.append(pizza[max_index])
    elif oteam2 > 0:
        oteam2 -= 1
        pizza2.append(pizza[max_index])
    else:
        break

    pizza.pop(max_index)
    ingredientcount.pop(max_index)
    differences.pop(max_index)
    count += 1

while len(pizza4) != 0:
    print("4", end=" ")
    count = 0
    for i in pizza4:
        print(temp3.index(i), end=" ")
        count += 1
        if (count == 4):
            break
    print()
    for j in range(4):
        pizza4.pop(0)

while len(pizza3) != 0:
    print("3", end=" ")
    count = 0
    for i in pizza3:
        print(temp3.index(i), end=" ")
        count += 1
        if (count == 3):
            break
    print()
    for j in range(3):
        pizza3.pop(0)
        
while len(pizza2) != 0:
    print("2", end=" ")
    count = 0
    for i in pizza2:
        print(temp3.index(i), end=" ")
        count += 1
        if (count == 2):
            break
    print()
    for j in range(2):
        pizza2.pop(0)
# # print(pizza4)
# # print(pizza3)
# # print(pizza2)

piz4 = []
piz3 = []
piz2 = []
for i in pizza4:
    piz4 += i;
for j in pizza3:
    piz3 += j
for k in pizza2:
    piz2 += k

# piz4 = set(piz4)
# piz3 = set(piz3)
# piz2 = set(piz2)

# score = len(set(piz4)) * len(set(piz4)) + len(set(piz3)) * len(set(piz3)) + len(set(piz2)) * len(set(piz2))
# print(f"score: {score}")
