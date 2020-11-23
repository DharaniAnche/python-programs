#swapping is an important concept when it comes to data strctures & algorithms
#normal way to swap
a=5
b=6
temporary_varible=a
a=b
b=temporary_varible
print(f'the value of a after swapping is {a}')
print(f'the value of b after swapping is {b}')
#python trick to swap
a,b=5,6
a,b=b,a
print(f'the value of a after swapping is {a}')
print(f'the value of b after swapping is {b}')