def welcome_text(request):
    
    twil = '''<?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Gather>"Welcome to the St. Louis Regional Municipal Court System Helpline! Please enter your citation number or driver's license number."</Gather>
            </Response>
            '''
    return HttpResponse(twil, content_type='application/xml', status=200)

