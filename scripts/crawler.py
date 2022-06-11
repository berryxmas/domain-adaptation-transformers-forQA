## This file contains the crawler class and the main function.

# import libraries
import pandas as pd
import numpy as np
import requests
import json
import time

# Specify base_url
base_url = "https://opendata.rijksoverheid.nl/v1/sources/rijksoverheid/infotypes/faq"
file_format = "json"

# Retrieve data via api and add to df
limit = 200
df_questions = pd.DataFrame()

# Loop through pages
for page_num in range(13): # 13 because 2500 QAs and 200 per request
    offset = page_num * limit
    url = base_url + f"?output={file_format}&offset={offset}&rows={limit}"
    print("Retrieving data from", url)
    df_temp = pd.read_json(url)
    df_questions = df_questions.append(df_temp)
    print("done.")

# Print amount of questions and timeframe
print("The amount of questions is " + str(len(df_questions)) + " and are asked between a timeframe from " + min(df_questions['lastmodified']) + " to " + max(df_questions['lastmodified']))

# Create empty df
df = pd.DataFrame()

# Loop through questions
for index, i in enumerate(df_questions['id']): #.head(20) for only first 20 samples
    url = base_url +"/"+ i+"?output="+file_format
    response = requests.get(url)
    df_temp = pd.json_normalize(response.json())
    df = df.append(df_temp)
    print("done with " + url)
    # sleep is needed for the api requests, otherwise it breaks
    if index % 100 == 0:
        time.sleep(60)
        print("sleeping, wait a moment plz")

# Save to csv
df.to_csv('policyqa-raw.csv', encoding = 'utf-8-sig') 
print("Saved to policyqa-raw.csv")