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



if __name__=="__main__":

    m = [[1, 2, 3], [4, 5], [6, 7, 8]]

    print(sum_zad4(m))