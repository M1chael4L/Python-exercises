import sys
sys.stdout.reconfigure(encoding='utf-8')

def zad3():
    n=int(input("Колко да е голям масива? "))
    m=[]
    for i in range(n):
        m.append(int(input))
    z=int(input("Колко да е z: "))
    statement=False
    for i in range(n):
        for j in range(i+1,n):
            if m[i]+m[j]==z:
                print("Има съвпадение")
                statement=True
                break
        if statement:
            break
    if statement==False:
        print("Няма съвпадение")
def sum_zad4(m):
    if len(m) == 0:
        return 0

    if type(m[0]) == list:
        return sum_zad4(m[0]) + sum_zad4(m[1:])

    return m[0] + sum_zad4(m[1:])
def zad5(n):
    if n==0:
        return 1
    else:
        return n*zad5(n-1)
        
def zad6(s, i=0, broi=0):
    if i == len(s):
        if broi == 0:
            return True
        else:
            return False

    if s[i] == '(':
        broi += 1

    elif s[i] == ')':
        broi -= 1

    if broi < 0:
        return False

    return zad6(s, i + 1, broi)

if __name__=="__main__":
    zad3()

    m = [[1, 2, 3], [4, 5], [6, 7, 8]]
    print(sum_zad4(m))

    n=int(input("Въведи число"))
    zad5(n)

    skobi=input("Въведи скоби: ")
    if zad6(skobi):
        print("Скобите са правилно въведени")
    else: 
        print("Скобите НЕ са правилно въведени")