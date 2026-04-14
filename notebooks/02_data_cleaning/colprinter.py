import pandas as pd

df = pd.read_csv(
    'D:\\DS-Proj-git\\ds-mini-project\\data\\merged\\merged_final.csv',
    low_memory=False
)

def print_unique_values_column(df, column_name, file):
    unique_values = df[column_name].unique()
    file.write(f"Unique values in column '{column_name}':\n")
    for value in unique_values:
        file.write(f"{value}\n")

# Open file in write mode
with open('unique_values_output_merged.txt', 'w', encoding='utf-8') as f:
    for col in df.columns:
        if col not in ["crm_membership_level"]:
            continue
        print_unique_values_column(df, col, f)
        f.write("\n\n")

print("Output saved to unique_values_output_merged.txt")