Допишите код функции penult_word() так, чтобы она возвращала третье с конца слово из любой фразы, переданной в аргументе.



quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    word = word_list[-3]
     
    return word

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))

