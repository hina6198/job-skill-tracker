from data.skills import SKILLS
import sqlite3
import pandas as pd


connection = sqlite3.connect("data/jobs.db")

df = pd.read_sql_query("SELECT * FROM jobs", connection)

skill_count = {}

for skill in SKILLS:
    count = 0

    for _, row in df.iterrows():

        text = f"{row['tags']} {row['description']}"

        if skill.lower() in text.lower():
            count += 1

    skill_count[skill] = count

result = (
    pd.DataFrame(
        skill_count.items(),
        columns=["Skill", "Count"]
    )
    .sort_values(
        by="Count",
        ascending=False
    )
)

print(result)

result.to_csv(
    "data/skill_frequency.csv",
    index=False
)

print("Saved skill_frequency.csv")