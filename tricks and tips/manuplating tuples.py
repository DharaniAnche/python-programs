#tuples are immutable
tuple1=(1,2,3,4,5)
print(type(tuple1))
list1=list(tuple1)
list1.append(6)
tuple2=tuple(list1)
print(tuple2)
print(type(tuple2))