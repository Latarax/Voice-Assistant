import os
from os.path import join

lookfor = "d7b42675-124b-4405-9fd2-9147015c7d9b.jpg"
for root, dirs, files in os.walk("D:\\"):
    print("searching", root)
    if lookfor in files:
        print("found %s" % join(root, lookfor))
        break
    else:
        print("Can't find file")