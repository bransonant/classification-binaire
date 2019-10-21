# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:13:50 2019

@author: Robin Chatelet & Antoine Branson
"""

import pandas as pd
# noinspection PyUnresolvedReferences
import pandas_profiling

dataFrame = pd.read_csv("antivirus_dataset.csv", delimiter='|', index_col=0)
profile = dataFrame.profile_report(title='Pandas Profiling Report')
rejected_variables = profile.get_rejected_variables(threshold=0.9)
profile.to_file(output_file="Pandas_profiling_report.html")
