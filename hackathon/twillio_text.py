"""
Examples to draw from

def twilio_text(request):
    
    twil = '''<?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Sms>Store Location: 123 Easy St. YO!</Sms>
            </Response>
            '''
    return HttpResponse(twil, content_type='application/xml', status=200)
    


Getting information from the user
    <Sms action="/smsHandler.php" method="GET">Store Location: 123 Easy St.</Sms>
"""


def auth_first_step(request):
    import pdb; pdb.set_trace()
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

