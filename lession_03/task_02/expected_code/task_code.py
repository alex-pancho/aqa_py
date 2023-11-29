def check_file_format(file_list: list, extention: str):
    new_list = []
    for i in file_list:
        if i.endswith(extention):
            new_list.append(i)

    return new_list


if __name__ == "__main__":
    file_list = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
    print(check_file_format(file_list, ".txt"))
    print(check_file_format(file_list, "json"))