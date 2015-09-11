from django.http import HttpResponse
import datetime
import json
from api.models import Fish

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)

def delete_fish(request):
    """
        Expects as input:
            - An id located in:
                - request.body if Angular.js
                - request.POST['id'] if backbone / jquery
    """
    fish_id = request.body #change this depending on how your frontend sends data, as POST or in the body

    Fish.objects.filter(id=fish_id).delete()
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def save_fish(request):
    """
        Expects as input:
            - A json string location in:
                - request.body if Angular.js
                - request.POST['fish_info'] if backbone / jquery
    """

    fish_info = request.body #change this depending on how your frontend sends data, as POST or in the body

    fsh = Fish(**json.loads(fish_info))
    fsh.save()
    return HttpResponse(json.dumps({
        "status": "success",
        "id": fsh.id,
        "data": list(Fish.objects.filter(id=fsh.id).values())[0] #lololol
    }, default=json_custom_parser), content_type='application/json', status=200)

def get_fish(request):
    fishies = Fish.objects.all()
    return HttpResponse(json.dumps({
        "status": "success",
        "data": list(fishies.values())
    }, default=json_custom_parser), content_type='application/json', status=200)
