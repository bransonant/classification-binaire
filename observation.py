# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:13:50 2019

@author: Robin Chatelet & Antoine Branson
"""

import numpy as np
import pandas as pd
import pandas_profiling

df = pd.read_csv(
        "antivirus_dataset.csv",  delimiter='|', index_col=0
)
profile = df.profile_report(title='Pandas Profiling Report')
profile.to_file(output_file="output.html")
print(df.sample(5))
