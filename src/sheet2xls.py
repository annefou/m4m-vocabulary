import pandas as pd
import os


file_name = os.environ['FILE_NAME']
sheet_id = os.environ["SHEET_ID"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={file_name}"

df = pd.read_csv(
    url, header=None, encoding="utf-8"
)

df.to_csv(file_name + ".csv", encoding="utf-8", header=False, index=False)

txt_delimiter = ","

largest_column_count = 0
with open(file_name + ".csv", "r") as temp_f:
    lines = temp_f.readlines()
    for l in lines:
        column_count = len(l.split(txt_delimiter)) + 1
        largest_column_count = (
            column_count
            if largest_column_count < column_count
            else largest_column_count
        )
temp_f.close()


column_names = [i for i in range(0, largest_column_count)]
print("column names = ", column_names)
df = pd.read_csv(
    file_name + ".csv", header=None, delimiter=txt_delimiter, names=column_names
)
df.to_excel(file_name + ".xlsx", index=False, header=False)


