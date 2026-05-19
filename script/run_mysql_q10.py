import pymysql
import pandas as pd
import time

# =========================================
# MySQL connection
# =========================================

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="tpch_sf001"
)

cursor = conn.cursor()

# =========================================
# Q10 Query
# =========================================

query = """
SELECT
    c_custkey,
    c_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue,
    c_acctbal,
    n_name,
    c_address,
    c_phone,
    c_comment
FROM
    customer,
    orders,
    lineitem,
    nation
WHERE
    c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND c_nationkey = n_nationkey
    AND o_orderdate >= DATE '1993-10-01'
    AND o_orderdate < DATE '1994-01-01'
    AND l_returnflag = 'R'
GROUP BY
    c_custkey,
    c_name,
    c_acctbal,
    n_name,
    c_address,
    c_phone,
    c_comment
ORDER BY
    revenue DESC
"""

# =========================================
# Execute
# =========================================

start = time.time()

cursor.execute(query)

results = cursor.fetchall()

end = time.time()

runtime = end - start

print("===================================")
print("Q10 Runtime:", runtime, "seconds")
print("Total Rows:", len(results))
print("===================================")

# =========================================
# Convert to dataframe
# =========================================

df = pd.DataFrame(results, columns=[
    "c_custkey",
    "c_name",
    "revenue",
    "c_acctbal",
    "n_name",
    "c_address",
    "c_phone",
    "c_comment"
])

# revenue 保留4位小数
df["revenue"] = df["revenue"].astype(float).round(4)

print(df)

# =========================================
# Save result
# =========================================

df.to_csv("mysql_q10_result_sf0.01.csv", index=False)

print("\nResult saved to mysql_q10_result.csv")

# =========================================
# Close connection
# =========================================

cursor.close()
conn.close()