#normal way
even_square=[]
for x in range(1,11):
    if x%2==0:
        even_square.append(x**2)
print(even_square)
#list_comprehension
even_square=[x**2 for x in range(1,11) if x%2==0]
print(f'printed using list_comprehension {even_square}')