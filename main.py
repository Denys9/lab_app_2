start = int(input('Введіть початкове число - '))
end = int(input("Введіть кінечне число - "))
if start%2==0:
    start +=1
while start < end:
    print(f"{start}")
    start +=2
else:
    print("Работа цикла завершена")
print("Работа программы завершена")