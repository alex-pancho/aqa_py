def change_params(old_value:str, new_value:str):
    filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""
    filetext = filetext.replace(old_value, new_value)
    return filetext


if __name__ == "__main__":
    print(change_params("800x600", "1024x800"))