Initialization
'''
User Input: Last name & Dob

User Output: ticket info or error if invalid data
'''

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