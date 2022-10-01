start = int(input("Введіть початкове числе - "))
end = int(input("Введіть кінцеве число - "))
if start %2==1:
    start += 1
while start < end:
    print(f"{start}")
    start += 2
else:
    print("Работа цикла завершена")
print("Работа программы завершена")