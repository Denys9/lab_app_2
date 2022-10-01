start = int(input("Введіть початкове число - "))
end = int(input("Введіть кінцеве число - "))
temp = start
start = end
end = temp
while start>end:
    start-=1
    print(f"{start}")
