import sys
import pandas as pd

usage = "python3 merge_csv.py [path_to_csv_file] [num_of_file]"
example = "python3 merge_csv.py ./HKTVMall/Customers_HKTVMall_tablet 2"

if len(sys.argv) < 3:
    print("Usage: " + usage)
    exit("Example: " + example)

file_prefix = sys.argv[1]
file_num = int(sys.argv[2])

all_files = []
for i in range(1, (file_num) + 1):
    file_name = file_prefix + str(i) + ".csv"
    all_files.append(file_name)

combined = pd.concat([pd.read_csv(f) for f in all_files])
file_name_combined = file_prefix + ".csv"
combined.to_csv(file_name_combined, sep=',', na_rep='N/A', encoding="utf_8_sig")