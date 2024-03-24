from tabulate import tabulate


def print_all_lexemes(tokens):
    lexemes = [(token.name,) for token in tokens]  # Создаем список лексем
    headers = ["Lexemes"]
    table = tabulate(lexemes, headers, tablefmt="grid")
    print(table)


def print_unique_tokens(tokens):
    unique_tokens = list({(token.name, token.type): token for token in tokens}.values())

    token_data = [(token.id, token.name, token.type, token.pos) for token in unique_tokens]
    headers = ["ID", "Name", "Type", "Position"]

    table = tabulate(token_data, headers=headers, tablefmt="grid")
    print(table)