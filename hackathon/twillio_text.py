
def twilio_text(request):
    
    twil = '''<xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Sms>Store Location: 123 Easy St.</Sms>
            </Response>
            '''
    return HttpResponse(twil, content_type='application/json', status=200)