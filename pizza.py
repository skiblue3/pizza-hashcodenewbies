pizzacount, team2, team3, team4 = [int(x) for x in input().split()]

ingredientcount = []
pizza = []

# reads input
# for i in range(pizzacount):
#     pizzalist = input().split()
#     ingredientcount.append(int(pizzalist[0]))
#     pizza.append(pizzalist[1:])

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

print(f"oteam2: {oteam2}, oteam3: {oteam3}, oteam4: {oteam4}")
