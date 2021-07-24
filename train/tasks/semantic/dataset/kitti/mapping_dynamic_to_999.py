import numpy as np
import glob as glob

path = glob.glob('/ws/external/infer_log/prediction_results/sequences/*/predictions/*.txt')
for file in path:
    pred_np = np.loadtxt(file)
    pred_np[pred_np == 1] = 999
    new_file = file.replace("map_exp1_log", "map_exp1_log2")
    np.savetxt(new_file, pred_np, fmt='%i')
