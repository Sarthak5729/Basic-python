my_list=['Lion','tiger','Elephant', 'Tiger' , 'Giraffe']
#first_element = my_list[2]
#print(first_element)
my_list.append('Zebra')
print(my_list)
print()
#remove
my_list.remove('Tiger')
print(my_list)
print()
#insert
my_list.insert(1 , 'Zebra')
print(my_list)
print()
#pop
poped_element =my_list.pop()
print(my_list)
print()
#sort
my_list.sort(key = str)
print(my_list)
print()
print('Elephant') in my_list

print(my_list[1:5])