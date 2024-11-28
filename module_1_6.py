#Практическое задание по теме: "Словари и множества"
my_dict={'BMW':1998, 'VW':2001, 'OPEL':2005}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['VW'])
print('Not existing value:', my_dict.get('AUDI'))
my_dict.update({'LADA':2015, 'GEELY':2020})
a=my_dict.pop('OPEL')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set={1,2,3,0.5,5,21,1,2,3,4,5,'steel'}
print ('Set:', my_set)
my_set.add(7), my_set.add(8),
my_set.discard(21)
print ('Modified set:',my_set)