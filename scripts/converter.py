# This file contains the converter for the annotated data to the model input

# Import libraries
import pandas as pd
import io
import json
import io

# Import data
df = pd.read_csv('../data/policyqa500.csv')
df = df[400:500]

# Lower case all answers
df["answer_short"] = df["answer_short"].str.lower()
df["introductioncontent"] = df["introductioncontent"].str.lower()

# Remove all non-alphanumeric characters
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r'<[^<>]*>', value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r'\[', value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r'\]', value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r'\{', value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r'\}', value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r"'", value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r"\\n", value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r"paragraph", value='', regex=True)
df["introductioncontent"] = df["introductioncontent"].replace(to_replace=r"paragraphtitle", value='', regex=True)

# Add all short answer character positions
a = []
for index, row in df.iterrows():
  b = str(df["introductioncontent"][index]).find(str(df["answer_short"][index]))
  a.append(b)

df["answer_start"] = a

# Save as df for eda
df.to_csv('../data/policyqa-annotated-clean.csv', encoding = 'utf-8-sig') 
print("Saved ../data/policyqa-annotated-clean.csv")

# Convert df to json model input
data = []
for index, row in df.iterrows():
    #print(row['id'])
    text = {
        "title": row['id'],
        "paragraphs": [
            {
                "qas": [
                    {
                        "question": row['question'],
                        "id": row['id'],
                        "answers": [
                            {
                                "text": row["answer_short"],
                                "answer_start": row['answer_start']
                            }
                        ]
                    }
                ],
                "context": row["introductioncontent"]
            }
        ]
    }
    data.append(text)

# Save as a more modern json file
with open('../data/dataTailv2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Saved to dataTailv2.json")