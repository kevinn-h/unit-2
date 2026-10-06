def wizard(N,start,duels):
    owner = start
    possessor = 1

    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            possessor += 1
    print(owner, possessor)



wizard(3,"A", ["BA","CB","DA"])