list=["yash","kunal",1212]
print(list)

list.append(1)
print(list)

list=[1,3,4,5,6]
print(list)
list.insert(1,2)
print(list)

list[2]=8
print(list)

list.extend([1,7,2,9,"yash"])
print(list)

print(list[3])

list.remove(5)
print(list)

list.pop()
print(list)

del list[3]
print(list)

print(len(list))

if 8 in list:
    print("element is present")
else:
    print("element is not present")

for i in list:
    print(i)

print(list.count(9))

print(list.index(9))

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list2=list.copy()
print(list2)

list.clear()
print(list)

