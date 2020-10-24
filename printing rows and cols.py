while 1:
    x=input()
    if x=='exit': break
    try:
        y=x.split()
        if y[0]=='numrows'or y[0]=='numcols':
            if y[1]=='test.txt'or y[1]=='anothertest.txt':  pass
            else:   print('File Not Found')
        else:   print("Incorrect command")
        f = y[1]
        try:
            if x!='exit':
                if y[0]=='numrows':
                    with open(f,"r")as Z:
                        i = sum(1 for l in Z)
                        print(i)
                else:
                    with open(f,"r") as Z:
                        y = [len(l.split()) for l in Z]
                        print(max(y))
        except: continue 
    except: continue