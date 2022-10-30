def get_count_char(str_): #функция частоты встречаемости каждого символа
    letter_dict = {}
    str_ = str_.lower() #переводим в нижний регистр

    for symbol in str_:
        if symbol.isalpha(): #поверяем, что символ - это буква
            letter_dict[symbol] = letter_dict.get(symbol, 0) + 1

    return letter_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


def percent_char(dict_percent): #функция для процентного соотношения
    dict_pr = {}
    sum_char = sum(dict_percent.values()) #считаем сумму всех знаков

    for char, amount in dict_percent.items():
        amount = round(amount / sum_char * 100, 2) #находим процентную долю и округляем
        dict_pr[char] = amount

    return dict_pr


print(get_count_char(main_str))
print(percent_char(get_count_char(main_str)))
