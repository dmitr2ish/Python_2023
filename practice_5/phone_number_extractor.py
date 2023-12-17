import re


class PhoneNumberExtractor:

    def find_phone_numbers(self, text):
        REG_EX_TWO_DIGIT = '\d{2}'  # две цифры
        REG_EX_THREE_DIGIT = '\d{3}'  # три цифры
        REG_EX_SPACE_HYPHEN_OPT = '[\s-]?'  # необязательный пробел или дефис
        REG_EX_SPACE_OPT = '\s?'  # не обязательный пробел
        REG_EX_PLUS_OPT = '\+?'  # не обязательный +
        REG_EX_AVAIBALE_COUNTRY_CODE = '[7843]'  # возможная первая цифра кода страны
        REG_EX_CITY_CODE = '(\(\d{3}\)|\d{3})'  # код города в скобках или без из 3х цифр

        # регулярное выражение для поиска телефонных номеров
        pattern = (REG_EX_PLUS_OPT
                   + REG_EX_AVAIBALE_COUNTRY_CODE
                   + REG_EX_SPACE_OPT
                   + REG_EX_CITY_CODE
                   + REG_EX_SPACE_HYPHEN_OPT
                   + REG_EX_THREE_DIGIT
                   + REG_EX_SPACE_HYPHEN_OPT
                   + REG_EX_TWO_DIGIT
                   + REG_EX_SPACE_HYPHEN_OPT
                   + REG_EX_TWO_DIGIT)

        # используем re.finditer для поиска всех совпадений
        phone_numbers = []
        for match in re.finditer(pattern, text):
            phone_numbers.append(match.group(0))

        return phone_numbers
