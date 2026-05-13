import pandas as pd
import glob

# load all files
files = glob.glob("data/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])

# clean column names
df.columns = df.columns.str.strip()

# normalize product text (VERY IMPORTANT)
df["product"] = df["product"].astype(str).str.strip().str.lower()

# filter correct product
df = df[df["product"] == "pink morsel"]

# clean price
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# ensure quantity is numeric
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# remove invalid rows
df = df.dropna(subset=["quantity", "price"])

# compute sales
df["Sales"] = df["quantity"] * df["price"]

# final output
output = df[["Sales", "date", "region"]]
output.columns = ["Sales", "Date", "Region"]

# save file
output.to_csv("formatted_output.csv", index=False)

print("Done - output created")