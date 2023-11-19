import re

def cleanser(input_string):
    processed_str = re.sub(r'[^\w\s]', ' ', input_string.replace('\n', ' '))
    return re.sub(r'\s+', ' ', processed_str).strip()

def splitter(input_string, sep):
    list_str = input_string.split(sep)
    return list_str, len(list_str)


def dictionary_counter(input_string, sep=' '):
    cleansed_list, length = splitter(cleanser(input_string), sep)
    dictionary = {}
    for word in cleansed_list:
        lower_word = word.lower()
        if lower_word in dictionary:
            dictionary[lower_word] += 1
        else:
            dictionary[lower_word] = 1
    return dict(sorted(dictionary.items()))

text = "Я помню чудное мгновенье:\n\
Передо мной явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
В томленьях грусти безнадежной,\n\
В тревогах шумной суеты,\n\
Звучал мне долго голос нежный\n\
И снились милые черты.\n\
\n\
Шли годы. Бурь порыв мятежный\n\
Рассеял прежние мечты,\n\
И я забыл твой голос нежный,\n\
Твои небесные черты.\n\
\n\
В глуши, во мраке заточенья\n\
Тянулись тихо дни мои\n\
Без божества, без вдохновенья,\n\
Без слез, без жизни, без любви.\n\
\n\
Душе настало пробужденье:\n\
И вот опять явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
И сердце бьется в упоенье,\n\
И для него воскресли вновь\n\
И божество, и вдохновенье,\n\
И жизнь, и слезы, и любовь."

print(dictionary_counter(text))