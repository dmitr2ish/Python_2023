from phone_number_extractor import PhoneNumberExtractor

case_1 = "\tPhone: +7 (948) 106 12 34.\n\
    Phone: +79481061234. \n\
    Phone: +7 948 106 12 34.\n\
    Phone: +7 (948) 106-12-34.\n\
    Phone: +7 (948) 1061234.\n\
    Phone: 8 (948) 106 12 34.\n\
    Phone: 89481061234.\n\
    Phone: 8(948)1061234.\n\
    Phone: +380713061234.\n\
    Phone:+446661061234\n\
    Not a Phone: +4466610612\n\
    Not a Phone: +44-666-106-12-34\n\
    Not a Phone: 4402 6661 0612 3400\n\
    Not a Phone: 666-10-12\n\
    Not a Phone: +44 (6661) 061 234\n\
    Not a Phone: +44 6661 061234\n"

print('Проверяем со следующим кейсом:\n{}\nОжидаем получить 10 номеров:'.format(case_1))

i = 0
for phone_number in PhoneNumberExtractor().find_phone_numbers(case_1):
    i += 1
    print('{}) {}'.format(i, phone_number))

print("Тест успешен: {}".format(i == 10))