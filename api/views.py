from django.http import HttpResponse
import datetime
import json
from api.models import Citation, Violation
from dateutil import parser

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)

def welcome(request):
    return HttpResponse(json.dumps({
            "message": "Welcome to the St. Louis Regional Municipal Court System Helpline! Please enter your citation number or driver's license number."
        }, default=json_custom_parser), content_type='application/json', status=200)

def get_info(request):

    if request.GET.get('citation', False) and request.GET.get('last_name', False) and request.GET.get('date_of_birth', False):

        citation_in_db = Citation.objects.filter(citation_number=request.GET['citation']).filter(last_name=request.GET['last_name']).filter(date_of_birth=parser.parse(request.GET['date_of_birth']))

    elif request.GET.get('drivers_license_number', False) and request.GET.get('last_name', False) and request.GET.get('date_of_birth', False):

        citation_in_db = Citation.objects.filter(drivers_license_number=request.GET['drivers_license_number']).filter(last_name=request.GET['last_name']).filter(date_of_birth=parser.parse(request.GET['date_of_birth']))

    else:
        
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Not enough information to authenticate user. Please pass in Date of Birth, Last Name, AND either driver's license number or citation number."
        }, default=json_custom_parser), content_type='application/json', status=200)



    if citation_in_db.exists():
        violation_in_db = Violation.objects.filter(citation_number=request.GET['citation'])
        return HttpResponse(json.dumps({
            "status": "success",
            "citation": list(citation_in_db.values())[0],
            "violation": list(violation_in_db.values())[0]
        }, default=json_custom_parser), content_type='application/json', status=200)
    else:
        #return error, not found
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Citation not found in database."
        }, default=json_custom_parser), content_type='application/json', status=200)



def auth_first_step(request):
    
    if request.GET.get('citation', False):

        citation_in_db = Citation.objects.filter(citation_number=request.GET['citation'])

    elif request.GET.get('drivers_license_number', False):

        citation_in_db = Citation.objects.filter(drivers_license_number=request.GET['drivers_license_number'])

    else:
        
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Citation Number or Driver's License not found in database."
        }, default=json_custom_parser), content_type='application/json', status=200)


    if citation_in_db.exists():
      
        return HttpResponse(json.dumps({
            "status": "success",
            "message": "Your Citation Number has been confirmed. Please send your last name and your date of birth."
        }, default=json_custom_parser), content_type='application/json', status=200)
    else:
        #return error, not found
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Citation not found in database."
        }, default=json_custom_parser), content_type='application/json', status=200)


    
def auth_second_step(request):
    if request.GET.get('last_name', False) and request.GET.get('date_of_birth', False):

        citation_in_db = Citation.objects.filter(last_name=request.GET['last_name']).filter(date_of_birth=parser.parse(request.GET['date_of_birth']))

    else:
        
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Not enough information to authenticate user. Please send your last name and date of birth."
        }, default=json_custom_parser), content_type='application/json', status=200)



    if citation_in_db.exists():
        violation_in_db = Violation.objects.filter(citation_number=request.GET['citation'])
        return HttpResponse(json.dumps({
            "status": "success",
            "citation": list(citation_in_db.values())[0],
            "violation": list(violation_in_db.values())[0]
        }, default=json_custom_parser), content_type='application/json', status=200)
    else:
        #return error, not found
        return HttpResponse(json.dumps({
            "status": "error",
            "message": "Citation not found in database."
        }, default=json_custom_parser), content_type='application/json', status=200)

def twilio(request):
    
    twil = '''<xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Say>Twilio can speak text.</Say>
                <Say voice="man">It can sound like a man.</Say>
                <Say voice="woman">Or a woman.</Say>
                <Say language="es">O habla en espanol.</Say>
                <Say voice="woman">Tada!</Say>
            </Response>'''
    return HttpResponse(twil, content_type='application/json', status=200)
