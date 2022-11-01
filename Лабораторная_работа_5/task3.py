import random


def get_unique_list_numbers(left_border=-10, right_border=10, list_size=15) -> list[int]:
    random_list = []
    while len(random_list) < list_size:
        i = random.randint(left_border, right_border)
        if i not in random_list:
            random_list.append(i)
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
