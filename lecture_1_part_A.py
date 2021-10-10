# Part A


def print_list(list_a):
    if len(list_a) <= 0:
        return

    print(list_a[0], end='')
    for x in range(1, len(list_a)):
        print(f", {list_a[x]}", end='')
    print()


def even_list(list_a):
    evens = []
    for a in list_a:
        if a % 2 == 0:
            evens.append(a)

    return evens


def generate_list(n):
    list_a = []

    for i in range(0, n):
        num = int(input(f"Insert a number to index {i}: "))
        list_a.append(num)

    return list_a


def intersection(list_a, list_b):
    new_list = []

    for a in list_a:
        for b in list_b:
            if a == b:
                new_list.append(a)
                break

    return new_list


def element_in_list(element, list_a):
    for a in list_a:
        if a == element:
            return True

    return False


def is_common(list_a, list_b):
    for a in list_a:
        if not element_in_list(a, list_b):
            return False

    for b in list_b:
        if not element_in_list(b, list_a):
            return False

    return True


def is_sudoku(matrix):
    all_elements = []

    for row in matrix:
        for element in row:
            all_elements.append(element)

    all_elements.sort()

    for i in range(1, 10): # run from 1 to 9
        if i != all_elements[i-1]:
            return False

    return True


def main():
    LIST = [1, 2, 3, 4, 6, 7, 8, 9]


    print("\nQ1:")
    print_list(LIST)

    print("\nQ2:")
    print_list(even_list(LIST))

    print("\nQ3:")
    length = int(input("Insert the list length: "))
    res_list = generate_list(length)
    print("You created the following list:")
    print_list(res_list)

    print("\nQ4:")
    LIST_B = [2, 3, 6, 8, 10, 11]
    print_list(intersection(LIST, LIST_B))

    print("\nQ5:")
    element = "Banana"
    general_list = ["Banana", "Apple", 2, "Peach"]
    print(element_in_list(element, general_list))
    print(element_in_list(3, LIST))
    print(element_in_list(3, even_list(LIST)))

    print("\nQ6:")
    print(is_common([1, 2, 3], [1, 2]))
    print(is_common(["Banana", "Apple", 2, "Peach"], ["Banana", "Apple", 2, "Peach"]))
    print(is_common(["Banana", "Apple", 2, "Peach"], ["Banana", "Apple", 1, "Peach"]))

    print("\nQ7:")
    matrix = [ [7, 8, 9],
               [3, 5, 2],
               [4, 1, 6]]
    print(f"Is sudoku? {is_sudoku(matrix)}")


if __name__ == '__main__':
    main()



