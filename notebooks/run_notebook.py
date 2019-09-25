#!/usr/bin/env python3
import papermill as pm
import pandas as pd
import os

groups = ['no secondary disability, english',
 'secondary disability, english',
 'no secondary disability, non-english',
 'secondary disability, non-english']

for g in groups:
    filename_stub = '-'.join(''.join([c for c in g if c!=',']).split(' '))
    try:
        pm.execute_notebook(
            'Enrollment Model.ipynb',
            'output/enrollment-{}.ipynb'.format(filename_stub),
            parameters=dict(group=g, filename_stub=filename_stub)
        )
    except Exception:
        print('{}-{}-{}.ipynb failed!'.format(h,c,b))
        os.system('rm hitters/{}-{}-{}.ipynb'.format(h,c,b))