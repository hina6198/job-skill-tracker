from data.skills import SKILLS
import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("data/jobs.db")

# Read all jobs
df = pd.read_sql_query("SELECT * FROM jobs", connection)
print(df.head())
results = []

# Get all unique roles
roles = df["role"].fillna("Unknown").unique()

# Count skills for each role
for role in roles:

    role_df = df[df["role"] == role]

    for skill in SKILLS:

        count = 0

        for _, row in role_df.iterrows():

            text = f"{str(row['tags'])} {str(row['description'])}"

            if skill.lower() in text.lower():
                count += 1

        results.append({
            "Role": role,
            "Skill": skill,
            "Count": count
        })

# Create DataFrame
result = pd.DataFrame(results)

# Sort data
result = result.sort_values(
    by=["Role", "Count"],
    ascending=[True, False]
)

# Save CSV
result.to_csv(
    "data/skill_frequency.csv",
    index=False
)

print(result.head())
print("Saved skill_frequency.csv")