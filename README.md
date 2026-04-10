# Customer Churn Analysis — DS Mini Project

## 📌 Overview
This project analyzes customer churn patterns using call center, billing, and communication data to understand why customers leave and predict future churn.

## 📂 Datasets
| Dataset | Description | Size |
|---------|-------------|------|
| `renewal_calls.csv` | Renewal call transcripts — churn reasons, complaints, competitor mentions | ~186K rows |
| `billings.csv` | Customer billing/payment history | ~43 MB |
| `cc_calls.csv` | Customer care/support call records | ~5 MB |
| `emails.csv` | Customer email communications | ~20 MB |

All datasets are linked by `Co_Ref` (Customer Reference ID).

## 📓 Notebooks (run in order)
1. `01_data_understanding.ipynb` — Explore and document all datasets
2. `02_data_cleaning.ipynb` — Clean and preprocess all datasets
3. `03_eda_visualization.ipynb` — Exploratory data analysis & charts
4. `04_feature_engineering.ipynb` — Create features and merge datasets
5. `05_modeling_evaluation.ipynb` — Build and evaluate churn prediction models

## 👥 Team
| Member | Responsibility |
|--------|---------------|
| Member 1 | Data Understanding |
| Member 2 | Data Cleaning & Preprocessing |
| Member 3 | EDA & Visualization |
| Member 4 | Feature Engineering & Merging |
| Member 5 | Modeling & Evaluation |

## ⚙️ Setup
```bash
pip install -r requirements.txt
```

## 🛠 Tech Stack
- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
