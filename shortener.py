import pandas as pd
import numpy as np
from IPython.display import display
import email
import json

filepath = "cleaned.csv"
emails = pd.read_csv(filepath)

countdf = {'humor':0, 'resumes':0, 'hr':0, 'personal':0, 'universities':0}

newdf = pd.DataFrame(columns = emails.columns)
leftoverdf = pd.DataFrame(columns = emails.columns)

for i in range(len(emails)):
    if emails.iloc[i]['X-Folder'] in list(countdf.keys()):
        countdf[emails.iloc[i]['X-Folder']] += 1
        if countdf[emails.iloc[i]['X-Folder']] <= 75:
            newdf = newdf.append(emails.iloc[i])
        else:
            leftoverdf = leftoverdf.append(emails.iloc[i])

print(countdf)
