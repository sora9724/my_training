my_dict = {'Andrew' : 1999, 'Sasha' : 2001, 'Masha' : 1998,}
print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get("Anton"))
my_dict.update({'Igor' : 2005,
                'Oleg': 1993})
a = my_dict.pop('Masha')
print(a)
print(my_dict)

my_set = {1, 'Груша', 1, 2.2, 2.2, 3,'Груша', 3, 3}
print(set(my_set))
my_set.add(14)
my_set.add(29)
my_set.remove('Груша')
print(my_set)


