def q1():
    print("Hello")

def q2():
    print("Hello World")

def q3():
    print("Hello")
    print("World")

def q4():
    print("'Hello'")

def q5():
    print('"Hello World"')

def q6():
    print('"!@#$%^&*()\'')

def q7():
    print('"C:\\Download\\\'hello\'.py"')

def q8():
    print('print("Hello\\nWorld")')

def q9():
    print(input())

def q10():
    print(int(input()))

def q11():
    print(float(input()))

def q12():
    print(input())
    print(input())

def q13():
    a = input()
    print(input())
    print(a)

def q14():
    a = input()
    print(a)
    print(a)
    print(a)

def q15():
    print('\n'.join(input().split()))

def q16():
    print(' '.join(input().split()[::-1]))

def q17():
    print((input()+' ')*3)

def q18():
    print(input())

def q19():
    print('-'.join(input().split('.')[::-1]))

def q20():
    print(input().replace('-', ''))

def q21():
    print('\n'.join(list(input())))

def q22():
    ymd = input()
    print(ymd[0:2], ymd[2:4], ymd[4:6])

def q23():
    print(input().split(':')[1])

def q24():
    print(input().replace(' ',''))

def q25():
    print(sum(list(map(int, input().split()))))

def q26():
    print(float(input())+float(input()))

def q27():
    print(hex(int(input()))[2:])

def q28():
    print(hex(int(input()))[2:].upper())

def q29():
    print(oct(int(input(), 16))[2:])

def q30():
    print(ord(input()))

def q31():
    print(chr(int(input())))

def q32():
    print(int(input())*-1)

def q33():
    print(chr(ord(input())+1))

def q34():
    a,b = list(map(int,input().split()))
    print(a-b)

def q35():
    a,b = list(map(float,input().split()))
    print(a*b)

def q36():
    s,n = input().split()
    print(s*int(n))

def q37():
    n = input()
    print(input()*int(n))

def q38():
    a,b = list(map(int,input().split()))
    print(a**b)

def q39():
    a,b = list(map(float,input().split()))
    print(a**b)

def q40():
    a,b = list(map(int,input().split()))
    print(a//b)

def q41():
    a,b = list(map(int,input().split()))
    print(a%b)

def q42():
    print("%.2f" % float(input()))

def q43():
    a,b = list(map(float,input().split()))
    print("%.3f" % (a/b))

def q44():
    a,b = list(map(int,input().split()))
    print(
        a+b,
        a-b,
        a*b,
        a//b,
        a%b,
        '%.2f'%(a/b)
    )

def q45():
    a,b,c = list(map(int,input().split()))
    print(a+b+c, '%.2f'%((a+b+c)/3))

def q46():
    print(int(input())<<1)

def q47():
    a,b = list(map(int, input().split()))
    print(a<<b)

def q48():
    a,b = list(map(int, input().split()))
    if a<b: print(True)
    else: print(False)

def q49():
    a,b = list(map(int, input().split()))
    if a==b: print(True)
    else: print(False)

def q50():
    a,b = list(map(int, input().split()))
    if b>=a: print(True)
    else: print(False)

def q51():
    a,b = list(map(int, input().split()))
    if a != b: print(False)
    else: print(True)

def q51():
    if input()=='0': print(True)
    else: print(False)

def q52():
    print(bool(int(input())))

def q53():
    print(not bool(int(input())))

def q54():
    a,b = list(map(lambda x:bool(int(x)), input().split()))
    print(a and b)

def q55():
    a,b = list(map(lambda x:bool(int(x)), input().split()))
    print(a or b)

def q56():
    a,b = list(map(lambda x:bool(int(x)), input().split()))
    print(a != b)

def q57():
    a,b = list(map(lambda x:bool(int(x)), input().split()))
    print(a == b)

def q58():
    a,b = list(map(lambda x:bool(int(x)), input().split()))
    print(not(a or b))

def q59():
    print(~int(input()))

def q60():
    a,b = list(map(int, input().split()))
    print(a&b)

def q61():
    a,b = list(map(int, input().split()))
    print(a|b)

def q62():
    a,b = list(map(int, input().split()))
    print(a^b)

def q63():
    print(max(list(map(int, input().split()))))

def q64():
    print(min(list(map(int, input().split()))))

def q65():
    a,b,c = list(map(int, input().split()))
    if a%2==0:
        print(a)
    if b%2==0:
        print(b)
    if c%2==0:
        print(c)

def q66():
    a,b,c = list(map(int, input().split()))
    if a%2==0:
        print('even')
    else:
        print('odd')
    if b%2==0:
        print('even')
    else:
        print('odd')
    if c%2==0:
        print('even')
    else:
        print('odd')

def q67():
    n = int(input())
    p = n>0
    e = n%2 == 0
    if not p and e:
        print('A')
    elif not p and not e:
        print('B')
    elif p and e:
        print('C')
    else:
        print('D')

def q68():
    n = int(input())
    if n >= 90:
        print('A')
    elif n>=70:
        print('B')
    elif n >= 40:
        print('C')
    else:
        print('D')

def q69():
    s = input()
    d = {
        'A': 'best!!!',
        'B': 'good!!',
        'C': 'run!',
        'D': 'slowly~',
    }
    if s not in ['A', 'B', 'C', 'D']:
        print('what?')
    else:
        print(d[s])

def q70():
    n = int(input())
    if n//3 == 1:
        print('spring')
    elif n//3 == 2:
        print('summer')
    elif n//3 == 3:
        print('fall')
    else:
        print('winter')

def q71():
    n = input()
    while n!='0':
        print(n)
        n = input()

def q72():
    for i in range(1, int(input())+1)[::-1]:
        print(i)

def q73():
    for i in range(int(input()))[::-1]:
        print(i)

def q74():
    for i in range(ord('a'), ord(input())+1):
        print(chr(i))

def q75():
    for i in range(int(input())+1):
        print(i)

def q76():
    for i in range(int(input())+1):
        print(i)

def q77():
    print(sum([i for i in range(1, int(input())+1) if i % 2 == 0]))

def q78():
    s=input()
    while s != 'q':
        print(s)
        s = input()
    print(s)

def q79():
    i = 1
    s = 0
    t = int(input())
    while t > s:
        s += i
        i += 1
    print(i-1) 

def q80():
    a,b = list(map(int, input().split()))
    for i in range(1, a+1):
        for j in range(1, b+1):
            print(i, j)

def q81():
    s = input()
    a = int(s, 16)
    for i in range(1,16):
        print('%s*%X=%X' % (s,i,a*i))

def q82():
    for i in range(1, int(input())+1) :
        if (i%10)==3 or (i%10)==6 or (i%10)==9 :
            print("X", end=' ')
        else:
            print(i, end=' ')
    print()

def q83():
    d=0
    a,b,c = list(map(int, input().split()))
    for i in range(a) :
        for j in range(b) :
            for k in range(c) :
                print(i, j, k)
                d+=1
    print(d)

def q84():
    h,b,c,s = list(map(int, input().split()))
    print('%.1f'%(h*b*c*s/8/1024/1024), 'MB')

def q85():
    w,h,b = list(map(int, input().split()))
    print('%.2f'%(w*h*b/8/1024/1024), 'MB')

def q86():
    i = 1
    s = 0
    t = int(input())
    while t > s:
        s += i
        i += 1
    print(s) 

def q87():
    for i in [i for i in range(1, int(input())+1) if i % 3 != 0]:
        print(i, end=' ')
    print()

def q88():
    a,d,n = list(map(int, input().split()))
    print(a+(n-1)*d)

def q89():
    a,r,n = list(map(int, input().split()))
    print(a*r**(n-1))

def q90():
    a,m,d,n = list(map(int, input().split()))
    for _ in range(n-1):
        a = a * m + d
    print(a)

def q91():
    a,b,c = list(map(int, input().split()))
    day=1
    while day%a!=0 or day%b!=0 or day%c!=0:
        day += 1
    print(day)

def q92():
    input()
    a = list(map(int, input().split()))

    for i in range(1, 24):
        print(a.count(i))

def q93():
    input()
    print(' '.join(input().split()[::-1]))

def q94():
    input()
    a = list(map(int, input().split()))
    print(min(a))

def q95():
    # 입력과정
    pos = [list(map(lambda x: int(x)-1, input().split())) for _ in range(int(input()))]
    for i in range(19):
        for j in range(19):
            if [i,j] in pos:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()

def q96():
    board = [input().split() for _ in range(19)]
    pos = [list(map(lambda x: int(x)-1, input().split())) for _ in range(int(input()))]
    for i in pos:
        for k in range(19):
            if board[i[0]][k] == '0':
                board[i[0]][k] = '1'
            else:
                board[i[0]][k] = '0'
            if board[k][i[1]] == '0':
                board[k][i[1]] = '1'
            else:
                board[k][i[1]] = '0'
    
    for i in board:
        print(' '.join(i))

def q97():
    h,w = list(map(int, input().split()))
    board = [[0 for j in range(w)] for i in range(h)]
    
    sticks = [list(map(int, input().split())) for _ in range(int(input()))]
    for stick in sticks:
        length = stick[0]
        if stick[1] == 0:
            for i in range(length):
                board[stick[2]-1][stick[3]-1+i] = 1
        else:
            for i in range(length):
                board[stick[2]-1+i][stick[3]-1] = 1

    for i in board:
        for j in i:
            print(j, end=' ')
        print()

def q98():
    board = [list(map(int, input().split())) for _ in range(10)]
    pos = [1,1] # y,x
    while True:
        board[pos[0]][pos[1]] = 9
        if board[pos[0]][pos[1]+1] == 1:
            pos = [pos[0]+1, pos[1]]
            if pos[0] == 9:
                break
        else:
            pos = [pos[0], pos[1]+1]
        if board[pos[0]][pos[1]] == 2:
            board[pos[0]][pos[1]] = 9
            break
        
    for i in board:
        for j in i:
            print(j, end=' ')
        print()
