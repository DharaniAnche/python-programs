def reverse(str):
    if len(str)<=1: return str
    return reverse(str[1:])+str[0]
print(reverse('king-kong-ding-dong'))

x = 'hello'
print(x[::-1])

x = 'hello'
for i in x[::-1]:
    print(i,end='')
