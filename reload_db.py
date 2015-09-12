import os, sys
import csv

#os.system("rm db.sqlite3") #Kill existing db
#os.system("rm -rf api/migrations/") #kill existing db definitions
#os.system("python manage.py migrate") #Create new db

sys.path.append("hackathon/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

from api.models import Citation, Violation
from dateutil import parser


print "~~~~~~~~~~~~~~~~~"
with open('citations.csv', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i +=1
        if i > 1:
            new_citation = Citation(**{
                "id": int(row[0]),
                "citation_number": int(row[1]),
                "citation_date": parser.parse(row[2]),
                "first_name": row[3],
                "last_name": row[4],
                "date_of_birth": parser.parse(row[5]),
                "defendant_address": row[6],
                "defendant_city": row[7],
                "defendant_state": row[8],
                "drivers_license_number": row[9],
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
                "warrant_status": False if row[4] == "False" else True,
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
