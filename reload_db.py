import os, sys
import csv

os.system("rm db.sqlite3") #Kill existing db
os.system("rm -rf api/migrations/") #kill existing db definitions
os.system("python manage.py migrate") #Create new db

sys.path.append("hackathon/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

from api.models import Citation, Violation
from dateutil import parser

def letter_to_number(l):
    if l in ['a', 'b', 'c']:
        return "2"
    elif l in ['d', 'e', 'f']:
        return "3"
    elif l in ['g', 'h', 'i']:
        return "4"
    elif l in ['j', 'k', 'l']:
        return "5"
    elif l in ['m', 'n', 'o']:
        return "6"
    elif l in ['p', 'q', 'r', 's']:
        return "7"
    elif l in ['t', 'u', 'v']:
        return "8"
    elif l in ['w', 'x', 'y', 'z']:
        return "9"
    return l


print "~~~~~~~~~~~~~~~~~"
with open('citations.csv', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i +=1
        if i > 1:
            last_name_phone = ""
            if row[4]:
                last_name_phone = "".join([letter_to_number(x) for x in row[4].lower()])
            drivers_license_number_phone = ""
            if row[9]:
                drivers_license_number_phone = "".join([letter_to_number(x) for x in row[9].lower()])
            new_citation = Citation(**{
                "id": int(row[0]),
                "citation_number": int(row[1]),
                "citation_date": parser.parse(row[2]),
                "first_name": row[3],
                "last_name": row[4],
                "last_name_phone": last_name_phone,
                "date_of_birth": parser.parse(row[5]),
                "defendant_address": row[6],
                "defendant_city": row[7],
                "defendant_state": row[8],
                "drivers_license_number": row[9],
                "drivers_license_number_phone": drivers_license_number_phone,
                "court_date": parser.parse(row[10]),
                "court_location": row[11],
                "court_address": row[12]
            })
            new_citation.save()
    print "Imported", i, "citations."

with open('violations.csv', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i +=1
        if i > 1:
            new_violation = Violation(**{
                "id": int(row[0]),
                "citation_number": int(row[1]),
                "violation_number": row[2],
                "violation_description": row[3],
                "warrant_status": False if row[4] == "FALSE" else True,
                "warrant_number": row[5],
                "status": row[6],
                "status_date": parser.parse(row[7]),
                "fine_amount": row[8].strip('$'),
                "court_cost": row[9].strip('$')
            })
            new_violation.save()
    print "Imported", i, "violations."

print "****Please run the below command to get create a user for the django admin panel"
print "python manage.py loaddata fixtures/superuser.json"
