import pandas as pd
from prettytable import PrettyTable
from colorama import Fore, Style

def print_colored_table(file_path):
    df = pd.read_excel(file_path)
    table = PrettyTable()

    table.field_names = [Fore.GREEN + column + Style.RESET_ALL for column in df.columns.tolist()]

    for index, row in df.iterrows():
        colored_row = []
        for item in row:
            if isinstance(item, str):
                colored_row.append(Fore.CYAN + str(item) + Style.RESET_ALL)
            elif isinstance(item, (int, float)):
                colored_row.append(Fore.RED + str(item) + Style.RESET_ALL)
            else:
                colored_row.append(str(item))
        table.add_row(colored_row)

    print(table)

if __name__ == "__main__":
    file_path = input("Path to Excel file: ")
    print_colored_table(file_path)
