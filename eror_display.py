def display_error(code, error_position):
    line, column = get_line_and_column(code, error_position)

    print("Ошибка в расстановке скобок:")
    for i, line_text in enumerate(code.splitlines(), start=1):
        print(f"{i}: {line_text}")
        if i == line:
            indicator = ' ' * column + '^'
            print(f"   {indicator}")

    print(f"Позиция ошибки: строка {line}, столбец {column + 1}.")  


def get_line_and_column(text, position):
    lines = text.splitlines()
    line_start = 0
    for i, line in enumerate(lines, start=1):
        line_end = line_start + len(line)
        if line_start <= position <= line_end:
            column = position - line_start
            return i, column
        line_start = line_end + 1  
    return -1, -1 