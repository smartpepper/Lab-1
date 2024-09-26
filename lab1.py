#Pertcev Andrey r3137 
from colorama import init, Fore, Back, Style
import time
import os
clear = lambda: os.system('cls')

def task1():
    init()
    print(Back.RED + '          ')
    print(Back.RED + '   ',Back.WHITE + ' ',Back.RED + '    ')
    print(Back.RED + ' ',Back.WHITE + '     ',Back.RED + '  ')
    print(Back.RED + '   ',Back.WHITE + ' ',Back.RED + '    ')
    print(Back.RED + '          ')
    print(Back.BLACK +' ')

def task2(n):
    for i in range (n):
        print("◯◯",end="")
    print()

def task3(m):
    for i in range(m):
        print()
        for j in range(m*2-1):
            if (j==0):
                print(m-i," ",end="")
            if (j==(m*2-2-i*2)):
                print("• ",end="")
            else:
                print("○ ",end="")
    print()
    print("   ",end="")
    for k in range(1,m*2):
        if k%2==1:
            if k<10:
                print(k,"  ",end="")
            else:
                print(k," ",end="")
    print()
    print("     ",end="")
    for k in range(1,m*2):
        if k%2==0:
            if k<10:
                print(k,"  ",end="")
            else:
                print(k," ",end="")
    print()
    print()

def task4():
    p=0
    with open('sequence.txt', 'r') as g:
        file = g.readlines()
    for number in file:
        if (float(number) >= (-3)) and (float(number)  <= (3)):
            p+=1
    percent = int(p/len(file)*100)
    for i in range(percent):
        print(Back.RED + ' ',end="")
    print(Back.BLACK +' Числа от -3 до 3 занимают ',percent,"%")
    for i in range(100-percent):
        print(Back.GREEN + ' ',end="")
    print(Back.BLACK +' Остальные числа занимают ',100-percent,"%")
    print()


def task5():
    print(" для запуска анимации введите любой символ в консоль")
    f=input()
    while True:
        print("Красивая")
        time.sleep(1)
        clear()
        print("анимация")
        time.sleep(1)
        clear()
        print("доступна")
        time.sleep(1)
        clear()
        print("каждому")
        time.sleep(1)
        clear()

    

task1()
task2(10)
task3(9)
task4()
task5()


