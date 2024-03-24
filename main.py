import re
from tabulate import tabulate
from Token_type import *
from similar import find_similar_word
from const import KEY_WORDS
from Token import *
from Lexer import Lexer
from eror_display import display_error
from output import print_all_lexemes, print_unique_tokens


def get_line_and_column(string, position):
    line = 1
    column = 1

    for i in range(position):
        if string[i] == '\n':
            line += 1
            column = 1
        else:
            column += 1

    return line, column

def get_token_type(token, token_types):
    for key, value in token_types.items():
        pattern = value.regex
        if re.fullmatch(pattern, token):
            return value
    return None

def print_leksemas(tokens):
    for token in tokens:
        if token != "undefined" and token.type.name == "identifier":
            print(token.id, end=' ')
        else:
            print(token.name, end=' ')


def main():
    leks = 0
    with open('input.txt', 'r', encoding='utf-8') as f:
        code = f.read()

    print('\n', code, '\n')
    lexer = Lexer(code)
    brackets_balanced, error_position = lexer.check_brackets()

    if not brackets_balanced:
        display_error(code, error_position)

    tokens = []
    specialCharsPattern = r"([\[\]{}()])"
    stringPattern = r'"(?:[^"])*"?'
    commentPattern = r';.*'
    otherPattern = r"[^\s \[\]{}()"";]*"
    combined_pattern = f"({specialCharsPattern}|{stringPattern}|{commentPattern}|{otherPattern})"

    regex = re.compile(combined_pattern)
    table_data = []
    tokens = []
    for match in regex.finditer(code):
        token = match.group(1)
        position = match.start()
        line, column = get_line_and_column(code, position)
        if token and token[0] != ';':
            token_type = get_token_type(token, TOKEN_TYPES)
            t = Token(token, token_type, position, leks)
            tokens.append(t)
            leks += 1
            table_data.append([t.name, t.type.name if t.type else "Unknown", line, column])
            if token not in KEY_WORDS:
                    similar_words = [word for word in find_similar_word(token, KEY_WORDS.keys()) if word != token]
                    if similar_words:
                        print(f"ОШИБКА '{token}': {', '.join(similar_words)}")
            if not t.type:
                    print(f"ОШИБКА '{t.name}': Unknown type")

    if tokens[0].name !='(':
        print(f"ОШИБКА '{tokens[0].name}': Код должен начинаться с символа '('")
    elif tokens[len(tokens)-1].name != ')':
        print(f"ОШИБКА '{tokens[len(tokens)-1].name}': Код должен заканчиваться символом ')'")

    # Вывод таблицы токенов
   # headers = ["Token", "Type", "Line", "Column"]
   # print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Вывод всех лексем
    lexemes_data = [(token.name,) for token in tokens]
    print(tabulate(lexemes_data, headers=["Lexemes"], tablefmt="grid"))

    # Вывод уникальных токенов

    # Убираем фильтрацию токенов с None, т.к. мы хотим отобразить их как 'Unknown'
    unique_tokens_data = list({(token.name, token.type): token for token in tokens}.values())

    # Используем тернарный оператор для замены None на 'Unknown' при создании unique_table_data
    unique_table_data = [
        (token.id,
         token.name,
         token.type.name if token.type is not None else 'Unknown',  # Заменяем None на 'Unknown'
         token.pos)
        for token in unique_tokens_data
    ]

    print(tabulate(unique_table_data, headers=["ID", "Name", "Type", "Position"], tablefmt="grid"))
if __name__ == "__main__":
        main()
