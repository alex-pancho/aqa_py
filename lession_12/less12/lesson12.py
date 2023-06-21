from pathlib import Path
import json

#indicate disk to work with
p = Path("d:\\")

#indicate path on disk to work with
p = p / "QA python" / "less12" 

#print([x for x in p.iterdir() if x.is_dir()]) #print all directories in path
#print([x for x in p.iterdir()]) #print everything in path
#print(p.parts) #print parts of path to directory
#print(p.parent) #print parent of path directory, can be p.parent.parent etc., also indexes can be used

p = p / "file.txt"
#print(p.suffixes) #prints extensions
#print(p.stem) #prints name of file without extension
#print(p.name) #full name of file

#also this can be used to iter files with needed extension via is_file
#print([x for x in p.iterdir() if x.is_dir()]) #print all directories in path

#print(Path.cwd()) #from where script runs, current work dir
#print(Path(__file__)) #current file

#print(p.home()) #C:\Users\vikwork

#print(p.exists()) #checks if file exists
#print(p.is_dir()) #or .is_file() shows true/false, whether path shows dir or file

#print([x for x in p.parent.iterdir()]) #iters all files in parent of p
#print([x for x in p.parent.glob("*.py")]) #iters by extension for p = p / "QA python" / "less12" / "ideas_for_test"

#(p.parent /"hillel").mkdir() #creates dir "hillel" in dir "ideas for test" 

# with p.open("r+", encoding="utf8") as file: #also open(p) can be used, r+ means we can read and write
    
#     file.writelines("\naa bb")
#     f = file.readline()

# print(f)

# with p.open("r", encoding="utf8") as file: #we open to read only, readlines makes dict
#     f = file.read()
# print(f)

#read, replace
# with p.open("r", encoding="utf8") as file: #also open(p) can be used, r+ means we can read and write
#     f = file.read()
# f = f.replace("Жили", "Поживали")
# print(f)

# with p.open("w", encoding="utf8") as file: #"w" deletes everything in file and re-writes it
#      file.write(f)

#modules to work with files

#json
# jjss = json.dumps({"c":0, "b":0, "a":0}, sort_keys=True, indent=4)
# #print(jjss)

# js = p.parent / "try.json"
# # with js.open("w") as file:
# #     file.write(jjss)

# with js.open() as file:
#     newfile = file.read()
# try:
#     my_read_json = json.loads(newfile) #read json file and make dict of it
# except json.decoder.JSONDecodeError:
#     my_read_json = ""

# print(newfile)

#csv
