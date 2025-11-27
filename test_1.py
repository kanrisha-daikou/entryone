import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entrypro.settings')
django.setup()

import pandas as pd
import sqlite3
from entry_app.models import ModelApp

file_name = 'db.sqlite3_2'
conn = sqlite3.connect(file_name)
curr = conn.cursor()

table_name = ModelApp._meta.db_table
print(table_name)
curr.execute(f'SELECT * FROM {table_name} LIMIT 1;')
column_names = [i[0] for i in curr.description]
print(column_names)

curr.close()