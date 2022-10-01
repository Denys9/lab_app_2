start = int(input('Введіть початкове число - '))
end = int(input("Введіть кінечне число - "))
if start>end:
    temp = start
    start = end
    end = temp
while start < end:
    start += 1
    print(f"{start}")
else:
    print("Работа цикла завершена")
print("Работа программы завершена")