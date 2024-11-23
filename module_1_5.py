#"Неизменяемые и изменяемые объекты. Кортежи и списки"
tuple=1,2,3,0.5,"apple",False
immutable_var=tuple
print("Immutable tuple:",immutable_var)
#immutable_var.append("ok")   =>   AttributeError:'tuple' object has no attribute 'append'
#immutable_var.extend(["nut"])  => AttributeError:'tuple' object has no attribute 'extend'
mutable_list=[1,2,3,0.5,"apple",False]
mutable_list.append("sun")
print("Mutable list:",mutable_list)




