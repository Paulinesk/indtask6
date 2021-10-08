print("Введите элементы массива: ")
while True:
    try:
        array = [int(x) for x in input().split()]
        break
    except ValueError:
        print("Вы должны ввести число, попробуйте снова.")
print(array)
while True:
    print("Введите delta: ")
    delta = input()
    if not delta.isdigit():
        print("Вы должны ввести число, попробуйте снова.")
    else:
        break
result = array.count(min(array) + int(delta))
print(result)