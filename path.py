import os

def dirname(path):
    return os.path.dirname(path)

def basename(path):
    return os.path.basename(path)

def extname(path):
    _,ext = os.path.splitext(path)
    return ext

# location = "/home/apple/Downloads/story.txt"
# dirloc = dirname(location)
# print(dirloc)
# filename = basename(location)
# print(filename)
# filext = extname(location)
# print(filext)