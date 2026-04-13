import pandas as pd

df = pd.read_csv(
    'C:\\Users\\MadanRajMA\\Documents\\DS-Proj\\ds-mini-project\\data\\cleaned\\billings_cleaned.csv',
    low_memory=False
)

def print_unique_values_column(df, column_name, file):
    unique_values = df[column_name].unique()
    file.write(f"Unique values in column '{column_name}':\n")
    for value in unique_values:
        file.write(f"{value}\n")

# Open file in write mode
with open('unique_values_output_billings.txt', 'w', encoding='utf-8') as f:
    for col in df.columns:
        if col in ["co_ref"]:
            continue
        print_unique_values_column(df, col, f)
        f.write("\n\n")

print("Output saved to unique_values_output.txt")