import csv
from collections import defaultdict
import sys

MYSQL_FILE = "cquirrel_q10_insert_sf0.01.csv"
GOLD_FILE = "mysql_q10_result_sf0.01.csv"
LOG_FILE = "eval_q10_insert_sf0.01.log"

SCHEMA = [
    "c_custkey",
    "c_name",
    "revenue",
    "c_acctbal",
    "n_name",
    "c_address",
    "c_phone",
    "c_comment"
]

# log helper
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


sys.stdout = Logger(LOG_FILE)

# utils
def is_number(x):
    try:
        float(x)
        return True
    except:
        return False


def key_of(row):
    return (row[0], row[1])


def match(a, b, tol=1.0):
    for i in range(len(a)):
        x, y = a[i], b[i]

        if is_number(x) and is_number(y):
            if abs(float(x) - float(y)) > tol:
                return False
        else:
            if x != y:
                return False
    return True


# 1. read fixed output
fixed = defaultdict(list)

with open(MYSQL_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        if len(row) < 9:
            continue

        data = row[:-1]
        ts = row[-1]

        if not ts.isdigit():
            continue

        fixed[key_of(data)].append((int(ts), data))


# 2. dedup (timestamp + revenue)
fixed_best = {}

for k, v in fixed.items():

    def sort_key(item):
        ts = item[0]
        data = item[1]

        try:
            rev = float(data[2])
        except:
            rev = float("-inf")

        return (ts, rev)

    best = max(v, key=sort_key)
    fixed_best[k] = best[1]


# 3. read gold
gold = []

with open(GOLD_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        gold.append(row)


# 4. evaluation
total = len(gold)
hit = 0
miss = []

print("========== Q10 EVALUATION ==========")

for g in gold:
    k = key_of(g)

    if k not in fixed_best:
        miss.append((g, "NOT FOUND"))
        continue

    pred = fixed_best[k]

    if match(g, pred):
        hit += 1
    else:
        miss.append((g, pred))


acc = hit / total if total > 0 else 0

print("TOTAL:", total)
print("HIT:", hit)
print("MISS:", len(miss))
print("ACCURACY:", acc)

print("\n========== ERROR SAMPLES ==========")

for i in range(min(10, len(miss))):
    print("\nGOLD:", miss[i][0])
    print("PRED:", miss[i][1])