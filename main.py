start = int(input('Введіть початкове число - '))
end = int(input("Введіть кінечне число - "))
if start>end:
    temp = start
    start = end
    end = temp
elif start%2==0:
        start +=1
while start < end:
    print(f"{start}")
    start +=1
else:
    print("Работа цикла завершена")
print("Работа программы завершена")