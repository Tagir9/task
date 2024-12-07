# "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = numbers = numbers[1:]

primes = []
not_primes = []

for i in a :
    flag = True
    for j in range((int(i/2)) , i) :
        if i % j == 0 :
            flag = False
            break
    if flag :
            primes.append(i)
    else :
            not_primes.append(i)

print ("Primes:", primes)
print ("Not Primes:",not_primes)

