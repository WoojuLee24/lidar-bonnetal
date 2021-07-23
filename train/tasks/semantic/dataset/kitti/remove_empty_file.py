import glob
import os

path = "/ws/data/KITTIMS/Map/sequences/*/labels/*.txt"
log = "/ws/data/KITTIMS/erased_filelist.txt"

paths = glob.glob(path)
empty_list = []
for file in paths:
    with open(file, 'r') as f:
        lines = f.readlines()
        if len(lines) == 0:
            with open(log, 'a') as g:
                g.write(file + "\n")
            mvfile = file.replace("labels", "velodyne")
            svfile = mvfile.replace("Map", "Scan")
            slfile = file.replace("Map", "Scan")
            # print(file)
            # print(mvfile)
            # print(svfile)
            # print(slfile)
            os.remove(file)
            os.remove(mvfile)
            os.remove(svfile)
            os.remove(slfile)
