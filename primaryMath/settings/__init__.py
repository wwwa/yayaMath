# coding: utf-8
"""
@author
@date
@content

"""
from .settings import *

try:
    from .settings_dev import *
except Exception as e:
    print(e)

print(DATABASES)
print(BASE_DIR)
print(PROJECT_DIR)