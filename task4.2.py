arr = []
for i in range(14):
    while True:
        try:
            num = int(input(f"Enter a number  {i+1}"))
            arr.append(num)
            break
        except ValueError:
            print("Ошибка!")
arr.append(sum(arr))
print('Ответ: ')
for num in arr:
    print(num, end = " ")
print()



