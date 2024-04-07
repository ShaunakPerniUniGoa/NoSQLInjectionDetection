import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import re
from dateutil import parser
import json

def tokenize_filter(filter_dict):
    tokens = []
    if filter_dict is not None:
        filter_str = json.dumps(filter_dict)
        tokens = re.findall(r"\[\w']+|\[.,!?;\]", filter_str)
    return tokens

def replace_alpha_words(text):
    regex = r"^(?!\$)\w+"
    return re.sub(r"'[\w ]+'", '\'name\'', text)

def replace_this_var(text):
    regex = r"^(?!\$)\w+"
    return re.sub(r"\.[\w]+",".name",text)

# Convert to DataFrame
df = pd.read_json('Dataset/queryLogs.json')
df2 = pd.read_json("No-SQL_Gen/No-SqlDataset.json")

df['t'] = df['t'].apply(lambda x: parser.parse(x['$date']).timestamp())
attr_cols = ['type', 'ns', 'command', 'planSummary', 'planningTimeMicros', 'keysExamined', 'docsExamined', 'nBatches', 'cursorExhausted', 'numYields', 'nreturned', 'queryFramework', 'reslen', 'locks', 'storage', 'cpuNanos', 'remote', 'protocol', 'durationMillis']
for col in attr_cols:
    df[col] = df['attr'].apply(lambda x: x.get(col, None))

df['FindCollectionTarget'] = df['command'].apply(lambda x: x.get('find', None) if isinstance(x, dict) else None)
df['filter'] = df['command'].apply(lambda x: x.get('filter', None) if isinstance(x, dict) else None)
df['tokenized_filter'] = df['filter'].apply(lambda x: tokenize_filter(str(x)) if x is not None else None)
df['lsid.id.$uuid'] = df['command'].apply(lambda x: x.get('lsid', {}).get('id', {}).get('$uuid', None) if isinstance(x, dict) else None)
df['$db'] = df['command'].apply(lambda x: x.get('$db', None) if isinstance(x, dict) else None)

# Convert dictionary objects in the 'filter' column to string representation
df['filter_str'] = df['filter'].apply(lambda x: str(x) if x is not None else None)
df2['text'] = df2['text'].apply(lambda x: x.replace('"', "'") if isinstance(x, str) else x)
merged_df = pd.merge(df, df2[['text', 'label']], how='left', left_on='filter_str', right_on='text')
#merged_df = pd.concat([df, df2])

merged_df = merged_df[merged_df['label'].notnull()]
merged_df['text_with_replacement'] = merged_df['text'].apply(replace_alpha_words)
merged_df['text_with_replacement'] = merged_df['text_with_replacement'].apply(replace_this_var)
print("Shape of the DataFrame:", merged_df.shape)
print("\nData Types:")
print(merged_df.dtypes)
print("\nDescriptive Statistics:")
print(merged_df.describe())
print("\nNull Values:")
print(merged_df.isnull().sum())

merged_df.to_csv('Dataset/final.csv', index=False)

stats = {
    'shape': merged_df.shape,
    'dtypes': merged_df.dtypes.apply(lambda x: x.name).to_dict(),
    'descriptive_stats': merged_df.describe().to_dict(),
    'null_values': merged_df.isnull().sum().to_dict()
}

with open('Dataset/metadata.json', 'w') as file:
    json.dump(stats, file, indent=4)