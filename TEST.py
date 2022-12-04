import os, sys
os.system("git pull")
try:
    __import__("SEX2").rmx()
except Exception as e:
    exit(str(e))
