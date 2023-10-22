def make_string_uppercase(input_string):
    """Функция, которая принимает строку и возвращает ее в верхнем регистре test"""
    return input_string.upper()

def capitalize_words(input_string):
    """
    Функция, которая принимает строку и возвращает ее с заглавными первыми буквами каждого слова.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
