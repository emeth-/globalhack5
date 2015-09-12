import os, sys

os.system("rm db.sqlite3")
os.system("python manage.py migrate")

