numbers=[1,2,3,4,5]
spellings=['one', 'two', 'three', 'four', 'five']
for number, spelling in zip(numbers, spellings):
    print(f'number {number} spelling is {spelling}')