import csv

INPUT = "output_q10_insert_sf0.01.csv"
OUTPUT = "cquirrel_q10_insert_sf0.01.csv"

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

NOISE = set([
    "CUSTKEY","C_NAME","C_ACCTBAL","C_PHONE",
    "N_NAME","C_ADDRESS","C_COMMENT","revenue"
])

def parse(line):
    line = line.strip().strip("()")
    parts = line.split("|")

    # remove empty
    parts = [p for p in parts if p != ""]

    # last element = timestamp (keep it)
    timestamp = parts[-1]

    # remove schema labels
    vals = [p for p in parts if p not in NOISE]

    return vals, timestamp


def fix_order(vals):
    """
    Cquirrel Q10 pattern inference:

    raw order often:
    0 custkey
    1 name
    2 acctbal
    3 phone
    4 nation
    5 address
    6 comment
    7 revenue
    """

    if len(vals) < 8:
        return None

    return {
        "c_custkey": vals[0],
        "c_name": vals[1],
        "c_acctbal": vals[2],
        "c_phone": vals[3],
        "n_name": vals[4],
        "c_address": vals[5],
        "c_comment": vals[6],
        "revenue": vals[7]
    }


with open(INPUT, "r", encoding="utf-8") as f, \
     open(OUTPUT, "w", newline="", encoding="utf-8") as out:

    writer = csv.writer(out)
    writer.writerow(SCHEMA + ["timestamp"])

    for line in f:
        if not line.strip():
            continue

        vals, ts = parse(line)
        row = fix_order(vals)

        if not row:
            continue

        writer.writerow([
            row["c_custkey"],
            row["c_name"],
            row["revenue"],
            row["c_acctbal"],
            row["n_name"],
            row["c_address"],
            row["c_phone"],
            row["c_comment"],
            ts   # 时间戳
        ])

print("done")