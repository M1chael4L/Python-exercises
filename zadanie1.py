import sys
sys.stdout.reconfigure(encoding='utf-8')

def zad1():
    print("КАЛКУЛАТОР")
    while True:
        symb=input("Избери изчисление: +, -, *, / или q-quit: ")
        if symb =="q":
            break
        if symb not in ["+","-","*","/"]:
            continue
        n1=float(input("Напиши първото число: "))
        n2=float(input("Напиши второто число: "))
        
        if symb =="+":
            print(f"Резултат: {n1+n2}")
        if symb =="-":
            print(f"Резултат: {n1-n2}")
        if symb =="*":
            print(f"Резлутат: {n1*n2}")
        if symb=="/":
            if n2==0:
                print("Не може да се дели на 0")
            else:
                print(f"Резултат: {n1/n2}")

def zad2_bez_cikli():
    d1={'а':1}
    d2={'б':2}
    d3={'в':3}

    list1=list(d1.items())
    list2=list(d2.items())
    list3=list(d3.items())

    merge_lists=list1+list2+list3
    merged=dict(merge_lists)

    print(merged)

zad1()

zad2_bez_cikli()