import numpy as np
import glob as glob

# path = glob.glob('/ws/external/infer_log/prediction_results/sequences/*/predictions/*.txt')
path = glob.glob("/ws/data/KITTIMapScan/Map/sequences/00/labels/*.txt")

sum_dynamic = 0
sum_static = 0

dynamic = 0
static = 0
false_dynamic = 0
for file in path:
    np_pred = np.loadtxt(file)
    for i in np_pred:
        if i in [252, 253, 254, 255, 256, 257, 258, 259]:
            dynamic += 1
        else:
            static += 1
    sum_dynamic += dynamic
    sum_static += static

print("dynamic length: ", sum_dynamic)
print("static length: ", sum_static)

# dynamic length:  188681393
# static length:  381459195503