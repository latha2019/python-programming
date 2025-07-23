# import os
#
# def dirname(path):
#     return os.path.dirname(path)
#
# def basename(path):
#     return os.path.basename(path)
#
# def extname(path):
#     _,ext = os.path.splitext(path)
#     return ext

def Filename(path):
    i = len(path)-1
    filename=""
    while i > 0:
        if path[i] == '/' or path[i] == '//':
            break

        filename = path[i] + filename
        i -= 1
    return filename

def dirname(path):
    i = len(path) - 1
    directory = ""
    while i > 0:
        if path[i] == '/' or path[i] == '//':
            break
        # filename = path[i] + filename
        i -= 1

    for j in range(i):
        directory += path[j]

    return directory

def extname(path):
    k = len(path) - 1
    filename = ""
    while k > 0:
        if path[k] == '/' or path[k] == '//':
            break
        filename = path[k] + filename
        k -= 1

    ext = filename.split(".")
    return ext[-1]

location = "/home/apple/Downloads/story.csv"
dirloc = dirname(location)
print(f"Directory: {dirloc}")
filename = Filename(location)
print(f"filename: {filename}")
filext = extname(location)
print(f"file ext: {filext}")
