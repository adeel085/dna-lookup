from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dnalookupapp.models import Protein
import json

# Create your views here.
@csrf_exempt
def filter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        look_key = data['code'].upper()
        proteins = Protein.objects.all()

        results = []
        found = False
        for p in proteins:
            seq = p.seq.upper()
            i = seq.find(look_key)
            while i != -1:
                found = True
                result = {
                    "name": p.name,
                    "ref": p.ref,
                    "seq": p.seq,
                    "index": i,
                    "id": data['id']
                }
                print("MATCH FOUND:" + seq[i - 11:i + 2])
                results.append(result)

                break
                i = seq.find(look_key, i + 1)
            if found:
                break
        response = {
            "data": results
        }

        print(response['data'][0]['index'])

        return JsonResponse(response)

@csrf_exempt
def sequence(request):
    print(request.method)
    if request.method == 'POST':
        data = json.loads(request.body)
        data["seq"] = data["seq"].rstrip("\n")
        print("DATA: ", data["seq"])
        protein = Protein(name=data["name"], ref = data["ref"], seq = data["seq"] )
        protein.save()
    return HttpResponse("request")