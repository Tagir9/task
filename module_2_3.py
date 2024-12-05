#"Стиль кода часть II. Цикл While"
a=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print("my_list =",a)
b=len(a)
i = 0
while i < b :
    if a[i] == 0 :
        i += 1
        continue
    if a[i] < 0 :
        break
    print (a[i])
    i += 1