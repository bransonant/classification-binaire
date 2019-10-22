# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:13:50 2019

@author: BRANSON Antoine & CHATELET Robin
"""

from common import data

profile = data.profile_report(title='Pandas Profiling Report')
rejected_variables = profile.get_rejected_variables(threshold=0.9)
profile.to_file(output_file="Pandas_profiling_report.html")
