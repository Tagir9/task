#"Базовые структуры данных."
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_names = sorted(students)
a = (sum(grades[0]))/len(grades[0])
b = (sum(grades[1]))/len(grades[1])
c = (sum(grades[2]))/len(grades[2])
d = (sum(grades[3]))/len(grades[3])
e = (sum(grades[4]))/len(grades[4])
dict={sorted_names[0]:a, sorted_names[1]:b, sorted_names[2]:c, sorted_names[3]:d, sorted_names[4]:e}
print(dict)