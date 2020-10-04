<<<<<<< HEAD
import pandas as pd
import numpy as np
from IPython.display import display
import email
import json

filepath = "cleaned.csv"
emails = pd.read_csv(filepath)

cat = input("Enter category:")
count = 4

for i in range(len(emails)):
    if emails.iloc[i]['X-Folder'] == cat:
        print(emails.iloc[i]['Message-Body'],emails.iloc[i]['Subject'])
        count -= 1
        if count == 0: break
=======
import pandas as pd
import numpy as np
from IPython.display import display
import email
import json

filepath = "cleaned.csv"
emails = pd.read_csv(filepath)

cat = input("Enter category:")
count = 4

for i in range(len(emails)):
    if emails.iloc[i]['X-Folder'] == cat:
        print(emails.iloc[i]['Message-Body'],emails.iloc[i]['Subject'])
        count -= 1
        if count == 0: break
>>>>>>> 65c1c1cebbe728ea79a841cb0075e400165f3530
