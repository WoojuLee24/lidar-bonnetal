import glob

path = "/ws/data/train_set/map/sequences"

paths = glob.glob(path + "/*/labels/*")
paths = sorted(paths)

length = 0
for file in paths:
    with open(file, 'r') as f:
        lines = f.readlines()
        if length < len(lines):
            length = len(lines)

print(length)