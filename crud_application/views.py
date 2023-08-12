import csv
import json
import os
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crud_application.models import *

@csrf_exempt
def add_student(request):
    try:
        response = JsonResponse({"message":""}, status = 200)
        request_object = json.loads(request.body)
        if all (key in request_object and request_object[key] for key in ["first_name", "last_name"]):
            student_obj = Student()
            student_obj.student_id = "ST" + str(int(time.time_ns()*10))
            student_obj.student_first_name = request_object["first_name"]
            student_obj.student_last_name = request_object["last_name"]
            student_obj.save()
            response = JsonResponse({"message":"Record inserted successfully"}, status = 200)
        else:
            response = JsonResponse({"message":"Invalid Request Object"}, status = 400)

    except Exception as error:
        print("Error in add_student: ",error)
        response = JsonResponse({"message":"sonething went wrong"}, status = 500)
    return response
