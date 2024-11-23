# "Динамическая типизация"
name="Artur"
print("Name:",name)
age=55
print("Age:",age)
new_age=56
print("New Age:",new_age)
print("Is Student:",(age!=new_age))#end

#"Переменные"
a=12    #Кол-во выполненных ДЗ
b=1.5   #Кол-во затраченных часов
course='Python' #Название курса
c=(b/a) #Время на одно задание
print("Курс:",course,", всего задач:",a,", затрачено часов:",b,", среднее время выполнения",c,"часа.")#end

#"Строки и индексация строк"
d='Топинамбур'
print(d[0])
print(d[-1])
e=int(len(d)/2)
print(d[e:])
print(d[::-1])
print(d[1::2])#end
