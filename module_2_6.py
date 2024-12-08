from random import randint
c_1 = randint(3,20) #cypher_1
print (c_1, "-число из первой вставки ")
c_2=[]

for i in range(1,c_1):
    for j in range(1,c_1):
        if c_1 % ( i + j ) == 0 and i!=j :
            a=sorted([i,j])
            if a not in c_2:
                c_2.append(a)

print(c_2,"- нужный пароль")

