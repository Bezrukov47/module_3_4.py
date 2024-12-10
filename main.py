def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру

    for word in other_words: # Перебираем подходящие слова
        # Приводим каждое слово к нижнему регистру и проверяем условиe
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено

    return same_words  # Возвращаем список подходящих/выбранных слов

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


# Выводим результаты на экран
print(result1)
print(result2)


