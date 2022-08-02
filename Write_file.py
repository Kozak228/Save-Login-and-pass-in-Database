from prettytable import PrettyTable, ALL, PLAIN_COLUMNS
from os import path

from Date_format import data

def write_file(datas, file_name):
    file_name += ".txt"
    table = PrettyTable(padding_width=2, hrules=ALL)
    table.field_names = ["Site", "Login", "Password"]
    table.set_style(PLAIN_COLUMNS)

    for i in datas:
        table.add_row(i[1:])

    if path.isfile(file_name):
        with open(file_name, "a") as f:
            f.write(f"*************************************| {data()} |********************************************************************\n")
            f.write(f"{table.get_string()}\n\n")
    else:
        with open(file_name, "w") as f:
            f.write(f"*************************************| {data()} |********************************************************************\n")
            f.write(f"{table.get_string()}\n\n")

    return "Information", f"Данные сохранены!\nCмотри файл '{file_name}' возле программы!"