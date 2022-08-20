rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
r = rec.copy()
print(id(r) == id(rec))

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)