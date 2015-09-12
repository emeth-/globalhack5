Initialization
'''
User inputting "ticket"
App outputting a welcome message + instructions
'''

def welcome(message)
#user sends "ticket"
 return HttpResponse(json.dumps({
            "message": "Welcome to yada. Please enter your citation number or driver's license number."
        }, default=json_custom_parser), content_type='application/json', status=200)
