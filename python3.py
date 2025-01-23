a=3+6j
b=5+7j
print(type(a))
print(type(b))
#mathematical operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#print(a//b) #unsupported 
print(63/2)
print(63//2)
print(63%2) #modules

#BOOLEANS-----> TRUE OR FALSE

password = 6589
print(password == 6589)
print(35>12)
print(35>35)
print(35>=35)

username = "sonia@23"
pin = "sonia@23"
if username == pin:
    print("success")
    if True:
        print("success")
print(int(True)) #value
print(int(False))

#list--- collection of elements
#list =[]
list_new= [2, 5, 6, "place", False, [1, 5, 6]]
print(list_new)
print(list_new[3])
print(len(list_new))
print(type(list_new)) #list
print(list_new[5: 9])
print(list_new[-6: -1])
print(list_new[-2: -5])
print(list_new[2: 3: 5])
print( list_new[5][2]) #list in list
#list is mutable
print(len(list_new[5]))
list_new[5][2] = "hello_world"
print(list_new) # list changed because list is mutable
list_new[4] = "True"
print(list_new)
variables =  list_new[5][1]
print(variables)

#TUPLE--> tuple is ordered collection of data items but immutable
#tuple memory is bit more than list memory
#list is slower than tuple
#list is mutable but tuple is immutable
tuple= (1, 2, 3.5, [6, 8, 9], "strings")
print(tuple)
print(tuple[3])
print(len(tuple))
print(tuple[-1])
print(tuple[-1][2])
#tuple[5] = "True"# immutable
#print(tuple) #imutable
print(list(range(0, 100)))
print(list(range(0, 100, 2)))
print(list(range(0, 100, 1)))
print(list(range(100, 0, -1)))
print(list(range(100, 0 -2)))



