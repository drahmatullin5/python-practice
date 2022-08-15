while True:
    try:
        numbers = input('Введите числа через пробел:   ')
        number_user = int(input('Введите любое число:  '))
        number_list = numbers.split()
        s = ''
        a = s.join(number_list)

        if " " not in numbers:
            print("\n введите числа через пробел!")
            continue
        elif a.isdigit():
            break
        else:
            print('Вводить нужно только цифры')
            continue
    except ValueError:
        print("Нужно ввести число!")



number_list = [int(item) for item in number_list]


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
number_list = merge_sort(number_list)
print(number_list)


def binary_search(number_list, number_user, left, right):
     if number_list[left]>number_user:
         return False

     middle = (right + left) // 2
     if number_list[middle] >= number_user:
         return middle
     elif number_user < number_list[middle]:
         return binary_search(number_list, number_user, left, middle - 1)
     else:
         return binary_search(number_list, number_user, middle + 1, right)


try:
    print("Позиция элемента меньше введенного числа:", binary_search(number_list, number_user, -1,  len(number_list)))
except IndexError:
    print('Число больше всех введенных чисел')
