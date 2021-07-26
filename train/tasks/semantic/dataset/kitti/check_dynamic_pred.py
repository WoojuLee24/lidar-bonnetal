import numpy as np
import glob as glob

# path = glob.glob('/ws/external/map_exp1_log2/prediction_results/sequences/*/predictions/*.txt')
path = glob.glob('/ws/external/map_exp1_log2/prediction_results/sequences/00/predictions/*.txt')
# path = glob.glob("/ws/external/infer_log/*.txt")

dynamic = 0
static = 0
false_dynamic = 0
for file in path:
    np_pred = np.loadtxt(file)
    dynamic += np.sum(np_pred == 999, axis=0)
    static += np.sum(np_pred == 0, axis=0)
    false_dynamic += np.sum(np_pred == 1, axis=0)
print("dynamic length: ", dynamic)
print("static length: ", static)
print("false dynamic length: ", false_dynamic)
