from pathlib import Path

# p = p / "file.txt"
# p = p / "hblog"
# print(p)
# print(p.suffixes)
# print((p.parent).suffixes) ## УВАГА бере суфікси зі шляху!!!
# print("stem:", p.stem) # Частина назви без розширення
# print(p.name)
print("cwd:", Path.cwd()) # current work dir
print("path_curreent file path_", Path(__file__)) # curreent file path
# print(p.home())  # user home
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
# print([x for x in p.parent.iterdir()])

def get_lines():

    filename = Path(__file__).parent.parent / "heartbeat" / "hblog"
    print("skf", filename)
    with open(filename, mode="r") as f:
        lines = f.readlines()
        return lines

print(get_lines())
