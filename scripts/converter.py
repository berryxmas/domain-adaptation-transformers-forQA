# This file contains the converter for the annotated data to the model input

# Import libraries
import pandas as pd
import io
import json
import io

# Import data
df = pd.read_csv('../data/policyqa-annotated.csv')
df = df.head(150)
df.head()

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

# Add all short answer character positions
a = []
for index, row in df.iterrows():
  b = df["introductioncontent"][index].find(df["answer_short"][index])
  a.append(b)

df["answer_start"] = a
df.head()

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
with open('../data/dataV3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Saved to dataV3.json")